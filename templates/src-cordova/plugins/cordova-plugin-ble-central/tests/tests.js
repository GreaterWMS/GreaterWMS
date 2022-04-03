exports.defineAutoTests = function () {

    describe('BLE object', function () {
        it("ble should exist", function () {
            expect(ble).toBeDefined();
        });

        it("should contain a startScan function", function () {
            expect(typeof ble.startScan).toBeDefined();
            expect(typeof ble.startScan).toBe("function");
        });
    });

};

exports.defineManualTests = function (contentEl, createActionButton) {

    createActionButton('Is Bluetooth Enabled?', function() {

        ble.isEnabled(
            function() {
                console.log("Bluetooth is enabled");
            },
            function() {
                console.log("Bluetooth is *not* enabled");
            }
        );
    });


    if (cordova.platformId !== 'ios') {

        // not supported on iOS
        createActionButton('Show Bluetooth Settings', function() {
            ble.showBluetoothSettings();
        });

        // not supported on iOS
        createActionButton('Enable Bluetooth', function() {

            ble.enable(
                function() {
                    console.log("Bluetooth is enabled");
                },
                function() {
                    console.log("The user did *not* enable Bluetooth");
                }
            );
        });

    }

    createActionButton('Scan', function() {

        var scanSeconds = 5;
        console.log("Scanning for BLE peripherals for " + scanSeconds + " seconds.");
        ble.startScan([], function(device) {
            console.log(JSON.stringify(device));
        }, function(reason) {
            console.log("BLE Scan failed " + reason);
        });

        setTimeout(ble.stopScan,
            scanSeconds * 1000,
            function() { console.log("Scan complete"); },
            function() { console.log("stopScan failed"); }
        );

    });

};
