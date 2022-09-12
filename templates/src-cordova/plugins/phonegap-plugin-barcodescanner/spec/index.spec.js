/* globals require */

/*!
 * Module dependencies.
 */

var cordova = require('./helper/cordova'),
    BarcodeScanner = require('../www/barcodescanner'),
    execSpy,
    execWin,
    options;

/*!
 * Specification.
 */

describe('phonegap-plugin-barcodescanner', function () {
    beforeEach(function () {
        execWin = jasmine.createSpy();
        execSpy = spyOn(cordova.required, 'cordova/exec').andCallFake(execWin);
    });

    describe('BarcodeScanner', function () {
      it("BarcodeScanner plugin should exist", function() {
          expect(BarcodeScanner).toBeDefined();
          expect(typeof BarcodeScanner == 'object').toBe(true);
      });

      it("should contain a scan function", function() {
          expect(BarcodeScanner.scan).toBeDefined();
          expect(typeof BarcodeScanner.scan == 'function').toBe(true);
      });

      it("should contain an encode function", function() {
          expect(BarcodeScanner.encode).toBeDefined();
          expect(typeof BarcodeScanner.encode == 'function').toBe(true);
      });

      it("should contain three DestinationType constants", function() {
          expect(BarcodeScanner.Encode.TEXT_TYPE).toBe("TEXT_TYPE");
          expect(BarcodeScanner.Encode.EMAIL_TYPE).toBe("EMAIL_TYPE");
          expect(BarcodeScanner.Encode.PHONE_TYPE).toBe("PHONE_TYPE");
          expect(BarcodeScanner.Encode.SMS_TYPE).toBe("SMS_TYPE");
      });
    });

    describe('BarcodeScanner instance', function () {
        describe('cordova.exec', function () {
            it('should call cordova.exec on next process tick', function (done) {
                BarcodeScanner.scan(function() {}, function() {}, {});
                setTimeout(function () {
                    expect(execSpy).toHaveBeenCalledWith(
                        jasmine.any(Function),
                        jasmine.any(Function),
                        'BarcodeScanner',
                        'scan',
                        jasmine.any(Object)
                    );
                    done();
                }, 100);
            });

            it('should call cordova.exec on next process tick', function (done) {
                BarcodeScanner.encode("", "",function() {}, function() {}, {});
                setTimeout(function () {
                    expect(execSpy).toHaveBeenCalledWith(
                        jasmine.any(Function),
                        jasmine.any(Function),
                        'BarcodeScanner',
                        'encode',
                        jasmine.any(Object)
                    );
                    done();
                }, 100);
            });
        });
    });
});
