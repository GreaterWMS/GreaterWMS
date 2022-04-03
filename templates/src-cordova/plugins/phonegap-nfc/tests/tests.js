exports.defineAutoTests = function () {
    
    describe('NFC object', function () {
        it("nfc should exist", function () {
            expect(nfc).toBeDefined();
        });

        it("should contain a addNdefListener function", function () {
            expect(typeof nfc.addNdefListener).toBeDefined();
            expect(typeof nfc.addNdefListener).toBe("function");
        });

        it("should contain a readerMode function", function () {
            expect(typeof nfc.readerMode).toBeDefined();
            expect(typeof nfc.readerMode).toBe("function");
        });

        it("should contain a transceive function", function () {
            expect(typeof nfc.transceive).toBeDefined();
            expect(typeof nfc.transceive).toBe("function");
        });
    });
    
    describe('UTF-8 Encoding and Decoding', function() {
        // https://github.com/don/ndef-js/blob/master/test/util.js

        it('should encode UTF-8', function() {

            var bytes=[ 0x54, 0x65, 0x73, 0x74, 0x73, 0xd7, 0x90, 0xc2, 0xa2];

            var encoded = util.stringToBytes("Testsא¢");
            expect(encoded).toEqual(bytes);

        });

        it('should decode UTF-8', function() {

            var bytes=[ 0x54, 0x65, 0x73, 0x74, 0x73, 0xd7, 0x90, 0xc2, 0xa2];

            var decoded = util.bytesToString(bytes);
            expect(decoded).toEqual("Testsא¢");

        });

        it('should encode and decode Russian', function() {

            // http://www.columbia.edu/~kermit/utf8.html
            var russian = "На берегу пустынных волн";
            var russianBytes = [ 0xD0, 0x9D, 0xD0, 0xB0, 0x20, 0xD0, 0xB1, 0xD0, 0xB5, 0xD1, 0x80, 0xD0, 0xB5,
                0xD0, 0xB3, 0xD1, 0x83, 0x20, 0xD0, 0xBF, 0xD1, 0x83, 0xD1, 0x81, 0xD1, 0x82, 0xD1, 0x8B, 0xD0,
                0xBD, 0xD0, 0xBD, 0xD1, 0x8B, 0xD1, 0x85, 0x20, 0xD0, 0xB2, 0xD0, 0xBE, 0xD0, 0xBB, 0xD0, 0xBD ];

            var encoded = util.stringToBytes(russian);
            expect(encoded).toEqual(russianBytes);
            

            var decoded = util.bytesToString(russianBytes);
            expect(decoded).toEqual(russian);
            
        });

        it('should round trip encode and decode UTF-8', function() {

            // http://www.columbia.edu/~kermit/utf8.html
            var chinese = "我能吞下玻璃而不伤身体。";
            var roundTrip = util.bytesToString(util.stringToBytes(chinese));
            expect(roundTrip).toEqual(chinese);

            var korean = "나는 유리를 먹을 수 있어요. 그래도 아프지 않아요";
            roundTrip = util.bytesToString(util.stringToBytes(korean));            
            expect(roundTrip).toEqual(korean);            

            var url = "http://example.com/with-utf8-✓";
            roundTrip = util.bytesToString(util.stringToBytes(url));                        
            expect(roundTrip).toEqual(url);

        });

    });

    describe('Translate ArrayBuffer and HEX Strings', function() {
        it('should convert array buffer to hex string', function() {
            var source = new Uint8Array([0x00, 0x01, 0x02, 0xFD, 0xFE, 0xFF]).buffer;
            var hexString = util.arrayBufferToHexString(source);
            expect(hexString).toEqual('000102fdfeff');
        });

        it('should convert hex string to array buffer', function() {

            var hexString = '000102FDFEFF'
            var buffer = util.hexStringToArrayBuffer(hexString);
            expect(new Uint8Array(buffer)).toEqual(new Uint8Array([0x00, 0x01, 0x02, 0xFD, 0xFE, 0xFF]));

            // leading 0
            var buffer = util.hexStringToArrayBuffer('0x68656c6c6f2c20776f726c64');
            expect(new Uint8Array(buffer)).toEqual(new Uint8Array([0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x2c, 0x20, 0x77, 0x6f, 0x72, 0x6c, 0x64]));

            // space delimiter
            var buffer = util.hexStringToArrayBuffer('68 65 6c 6c 6f 2c 20 77 6f 72 6c 64');
            expect(new Uint8Array(buffer)).toEqual(new Uint8Array([0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x2c, 0x20, 0x77, 0x6f, 0x72, 0x6c, 0x64]));

            // : delimiter
            var buffer = util.hexStringToArrayBuffer('68:65:6c:6c:6f:2c:20:77:6f:72:6c:64');
            expect(new Uint8Array(buffer)).toEqual(new Uint8Array([0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x2c, 0x20, 0x77, 0x6f, 0x72, 0x6c, 0x64]));

            // - delimiter
            var buffer = util.hexStringToArrayBuffer('68-65-6c-6c-6f-2c-20-77-6f-72-6c-64');
            expect(new Uint8Array(buffer)).toEqual(new Uint8Array([0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x2c, 0x20, 0x77, 0x6f, 0x72, 0x6c, 0x64]));
            
        });
    });

    describe('nfc.transceive', function() {

        it('should reject invalid input', function(done) {
            var promise = nfc.transceive(42);
            
            promise.then(
                function resolve() {
                    throw new Error('Promise should not be resolved');
                },
                function reject(reason) {
                    expect(reason).toBe("Expecting an ArrayBuffer or String");
                    done();
                }
            )
        });

    });

};

exports.defineManualTests = function (contentEl, createActionButton) {
    // TODO
};