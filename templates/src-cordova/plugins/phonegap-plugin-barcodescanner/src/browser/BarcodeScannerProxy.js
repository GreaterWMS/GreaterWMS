function scan(success, error) {
    var code = window.prompt("Enter barcode value (empty value will fire the error handler):");
    if(code) {
        var result = {
            text:code,
            format:"Fake",
            cancelled:false
        };
        success(result);
    } else {
        error("No barcode");
    }
}

function encode(type, data, success, errorCallback) {
    success();
}

module.exports = {
    scan: scan,
    encode: encode
};

require("cordova/exec/proxy").add("BarcodeScanner",module.exports);