/* globals:  export, module, console, document, ndef, Windows, Uint8Array */

"use strict";

var STATUS_NFC_OK = "NFC_OK";
var STATUS_NO_NFC = "NO_NFC";
var STATUS_NFC_DISABLED = "NFC_DISABLED";
// I don't think there is a Windows API to determine if NFC exists
var STATUS_NO_NFC_OR_NFC_DISABLED = "NO_NFC_OR_NFC_DISABLED";
var STATUS_NDEF_PUSH_DISABLED = "NDEF_PUSH_DISABLED";

var ndefUtils = {
    // convert Uint8Array to []
    toArray: function (bytes) {
        var output = [], i = 0;
        for (; i < bytes.length; i += 1) {
            output.push(bytes[i]);
        }

        return output;
    }
};

var self = {
    subscribedMessageId: -1,
    publishedMessageId: -1,
    proximityDeviceStatus: STATUS_NO_NFC_OR_NFC_DISABLED,
    listeningForNonNdefTags: false,
    tagEventTimeoutId: -1,
    initializeProximityDevice: function() {
        if (self.proximityDevice) {
            // TODO Is there an API to tell if the user disabled NFC?
            try {
                // KLUDGE this call fails when the user has disabled the device
                var kludge = self.proximityDevice.maxMessageBytes;
                self.proximityDeviceStatus = STATUS_NFC_OK;
            } catch (e) {
                console.log(e);
                self.proximityDeviceStatus = STATUS_NFC_DISABLED;
            }
            return self.proximityDeviceStatus === STATUS_NFC_OK;
        }

        // try to get device again because user might have re-enabled the device
        self.proximityDevice = Windows.Networking.Proximity.ProximityDevice.getDefault();

        // TODO use these events to implement nfc.addTagDiscoveredListener
        if (self.proximityDevice) {
            self.proximityDevice.ondevicearrived = function (eventArgs) {
                console.log("NFC tag detected");
                if (self.listeningForNonNdefTags) {
                    // set a timeout so NDEF tags can cancel this event
                    // we want one event to mimic the Android behavior
                    self.tagEventTimeoutId = setTimeout(self.fireTagEvent, 100);
                }
            };

            self.proximityDevice.ondevicedeparted = function (eventArgs) {
                console.log("NFC tag is gone");
            };
        } else {
            self.proximityDeviceStatus = STATUS_NO_NFC_OR_NFC_DISABLED;
        }

        return self.proximityDeviceStatus === STATUS_NFC_OK;
    },
    init: function (success, failure, args) {

        self.initializeProximityDevice();

        if (!self.proximityDevice) {
            console.log("WARNING: proximity device is null");
        }

        success();
    },
    registerNdef: function (success, failure, args) {
        console.log("Listening for NFC tags with NDEF messages.");

        if (!self.initializeProximityDevice()) {
            failure(self.proximityDeviceStatus);
            return;
        }

        try {
            self.subscribedMessageId = self.proximityDevice.subscribeForMessage("NDEF", self.messageReceivedHandler);
            success();
        } catch (e) {
            console.log(e);
            failure(e);
        }
    },
    removeNdef: function (success, failure, args) {

        console.log("Removing NDEF Listener");

        if (!self.initializeProximityDevice()) {
            failure(self.proximityDeviceStatus);
            return;
        }

        try {
            if (self.subscribedMessageId !== -1) {
                self.proximityDevice.stopSubscribingForMessage(self.subscribedMessageId);
                self.subscribedMessageId = -1;
            }

            success();
        } catch (e) {
            console.log(e);
            failure(e.message);
        }
    },
    addTagDiscoveredListener: function(success, failure, args) {
        self.listeningForNonNdefTags = true;
        success();
    },
    remoteTagDiscoveredListener: function(success, failure, args) {
        self.listeningForNonNdefTags = false;
        success();
    },
    writeTag: function (success, failure, args) {

        console.log("Write Tag");

        if (!self.initializeProximityDevice()) {
            failure(self.proximityDeviceStatus);
            return;
        }

        try {
            var records = args[0];
            var bytes = ndef.encodeMessage(records);

            self.stopPublishing();

            var dataWriter = new Windows.Storage.Streams.DataWriter();
            dataWriter.unicodeEncoding = Windows.Storage.Streams.UnicodeEncoding.utf16LE;
            dataWriter.writeBytes(bytes);

            self.publishedMessageId = self.proximityDevice.publishBinaryMessage("NDEF:WriteTag",
                dataWriter.detachBuffer(),
                function (sender, messageId) {
                      console.log("Successfully wrote message to the NFC tag.");
                      self.stopPublishing();

                      success();
                }
            );

        } catch (e) {
            console.log(e);
            failure(e.message);
        }
    },
    shareTag: function(success, failure, args) {

        console.log("Share Tag");

        if (!self.initializeProximityDevice()) {
            failure(self.proximityDeviceStatus);
            return;
        }

        try {
            var records = args[0];
            var bytes = ndef.encodeMessage(records);

            self.stopPublishing();

            var dataWriter = new Windows.Storage.Streams.DataWriter();
            dataWriter.unicodeEncoding = Windows.Storage.Streams.UnicodeEncoding.utf16LE;
            dataWriter.writeBytes(bytes);

            self.publishedMessageId = self.proximityDevice.publishBinaryMessage("NDEF",
                dataWriter.detachBuffer(),
                function (sender, messageId) {
                    console.log("Successfully shared message over peer-to-peer.");
                    self.stopPublishing();

                    success();
                });

        } catch (e) {
            console.log(e);
            failure(e.message);
        }
    },
    unshareTag: function(success, failure, args) {
        console.log("Unshare Tag");

        if (!self.initializeProximityDevice()) {
            failure(self.proximityDeviceStatus);
            return;
        }

        try {
            self.stopPublishing();
            success();
        } catch (e) {
            console.log(e);
            failure(e.message);
        }
    },
    enabled: function(success, failure, args) {
        self.initializeProximityDevice();

        if (self.initializeProximityDevice()) {
            success();
        } else {
            failure(self.proximityDeviceStatus);
        }

    },
    showSettings: function(success, failure, args) {

        // WARNING: this isn't documented, so it might break
        var nfcSettingsUri = "ms-settings-proximity:";
        var uri = new Windows.Foundation.Uri(nfcSettingsUri);

        Windows.System.Launcher.launchUriAsync(uri).then(
            function (settingsAppeared) {
                if (settingsAppeared) {
                    success();
                } else {
                    failure();
                }
            }
        );
    },
    stopPublishing: function() {
        if (self.publishedMessageId !== -1) {
            self.proximityDevice.stopPublishingMessage(self.publishedMessageId);
            self.publishedMessageId = -1;
        }
    },
    messageReceivedHandler: function (sender, message) {

        // this is an NDEF message so cancel the tag event before it fires
        clearTimeout(self.tagEventTimeoutId);

        var bytes = new Uint8Array(message.data.length);
        var dataReader = Windows.Storage.Streams.DataReader.fromBuffer(message.data);
        dataReader.readBytes(bytes);
        dataReader.close();

        var byteArray = ndefUtils.toArray(bytes);
        var ndefMessage = ndef.decodeMessage(byteArray);
        console.log(JSON.stringify(ndefMessage));

        // on windows, tag only contains the ndef message
        // other platforms have tag data
        var tag = {
            ndefMessage: ndefMessage
        };

        // fire JavaScript event with NDEF data
        var e = document.createEvent('Events');
        e.initEvent("ndef", true, false);
        e.tag = tag;
        document.dispatchEvent(e);
    },
    fireTagEvent: function() {
        var e = document.createEvent('Events');
        e.initEvent("tag", true, false);
        // unfortunately we don't have any tag metadata
        e.tag = {};
        document.dispatchEvent(e);
    }
};

module.exports = {
    init: self.init,
    registerNdef: self.registerNdef,
    removeNdef: self.removeNdef,
    registerTag: self.addTagDiscoveredListener,
    remoteTag: self.removeTagDiscoveredListener,
    writeTag: self.writeTag,
    shareTag: self.shareTag,
    unshareTag: self.unshareTag,
    enabled: self.enabled,
    showSettings: self.showSettings
}

require("cordova/exec/proxy").add("NfcPlugin", module.exports);
