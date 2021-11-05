/*jshint quotmark:double, strict:false, bitwise: false */
/*global PluginResult */

// based on code from Gord Tanner https://github.com/chariotsolutions/phonegap-nfc/pull/32

var alphabet = "ABCDEFGHIJKLM" +
               "NOPQRSTUVWXYZ" +
               "abcdefghijklm" +
               "nopqrstuvwxyz" +
               "0123456789+/=";

function b64toArray(input) {
    var result = [],
        workValue = [],
        bytes = [],
        offset = 0;

    while (offset < input.length) {
        for (var i = 0; i < 4; ++i) {
            if (offset >= input.length) {
                workValue[i] = 64;
            } else {
                var index = alphabet.indexOf(input.substring(offset++, offset));
                if (index === -1) {
                    --i;
                    continue;
                }
                workValue[i] = index;
            }
        }
        bytes[0] = (workValue[0] << 2 | workValue[1] >> 4) & 255;
        bytes[1] = (workValue[1] << 4 | workValue[2] >> 2) & 255;
        bytes[2] = (workValue[2] << 6 | workValue[3]) & 255;

        if (workValue[3] === 64 && workValue[2] === 64) {
            result.push(bytes[0]);
        } else if (workValue[3] === 64) {
            result.push(bytes[0]);
            result.push(bytes[1]);
        } else {
            result.push(bytes[0]);
            result.push(bytes[1]);
            result.push(bytes[2]);
        }
    }

    return result;
}

function decodeNdefRecord(encoded) {

    var ndefRecord = {
            tnf: encoded[0] & 7
        },
        flags = encoded[0],
        isShortRecord = (flags & 16) !== 0, //  short record
        hasIdLength = (flags & 8) !== 0, // identification length
        offset = 1,
        typeLength = encoded[offset++],
        idLength = 0,
        payloadLength = 0;

    if (isShortRecord) {
        payloadLength = encoded[offset++];
    } else {
        for ( var i = 0; i < 4; ++i) {
            payloadLength *= 256;
            payloadLength |= encoded[offset++];
        }
    }

    if (hasIdLength) {
        idLength = encoded[offset++];
    }

    ndefRecord.type = encoded.slice(offset, offset + typeLength);

    offset += typeLength;
    ndefRecord.id = encoded.slice(offset, offset + idLength);

    offset += idLength;
    ndefRecord.payload = encoded.slice(offset, offset + payloadLength);

    return ndefRecord;
}

function decode(encoding) {
    var decoded = [];
    var offset = 0;

    while (offset < encoding.length) {
        var start = offset;
        var remaining = encoding.length - offset;
        var flags = encoding[offset++];
        var minLength = 1 + 1;
        var sr = (flags & 16) !== 0;
        var il = (flags & 8) !== 0;

        minLength += sr ? 1 : 4;
        minLength += il ? 1 : 0;
        if (minLength <= remaining) {
            var typeLength = encoding[offset++];
            var payloadLength = 0;
            if (sr) {
                payloadLength = encoding[offset++];
            } else {
                for ( var i = 0; i < 4; ++i) {
                    payloadLength <<= 8;
                    payloadLength |= encoding[offset++];
                }
            }
            var idLength = il ? encoding[offset++] : 0;
            var totalLength = minLength + typeLength + payloadLength + idLength;
            if (totalLength <= remaining) {
                var encoded = encoding.slice(start, start + totalLength);

                decoded.push(decodeNdefRecord(encoded));

                offset = start + totalLength;
            }
        }
    }
    return decoded;
}

// called by invoke, when NFC tag is scanned
var tagListener = function(pluginResult, payloadString) {
    var payload = JSON.parse(payloadString),
        ndefObjectAsString = JSON.stringify(decode(b64toArray(payload.data)));
    pluginResult.callbackOk(ndefObjectAsString, true);
};

module.exports = {
    init: function(success, failure, args, env) {
        // no-op, just here for Android compatibility
        var result = new PluginResult(args, env);
        result.ok();
    },
    registerNdef: function(success, failure, args, env) {

        var result = new PluginResult(args, env),
            application = window.qnx.webplatform.getApplication(),
            ndefListener = tagListener.bind(null, result);

        application.invocation.addEventListener("invoked", ndefListener);
        result.noResult(true);
    }
};
