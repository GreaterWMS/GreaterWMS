# Getting Started with PhoneGap NFC on BlackBerry 10

Hardware & Software
 * OSX 10.10.5 
 * BB10 WebWorks SDK 2.2.0.15
 * Cordova 5.5.3
 * PhoneGap NFC 0.6.5
 * BlackBerry Z10 running 10.3.1.156

Create the project and install the plugins

    cordova create nfc com.example.nfc HelloNFC
    cd nfc
    cordova platform add blackberry10
    cordova plugin add phonegap-nfc
    cordova plugin add cordova-plugin-bb-invoke

edit `www/js/index.js` and replace `onDeviceReady` with

    onDeviceReady: function() {
        app.receivedEvent('deviceready');

        // Read NDEF formatted NFC Tags
        nfc.addNdefListener (
            function (nfcEvent) {
                var tag = nfcEvent.tag,
                    ndefMessage = tag.ndefMessage;

                // dump the raw json of the message
                // note: real code will need to decode
                // the payload from each record
                alert(JSON.stringify(ndefMessage));

                // assuming the first record in the message has
                // a payload that can be converted to a string.
                alert(nfc.bytesToString(ndefMessage[0].payload).substring(3));
            },
            function () { // success callback
                alert("Waiting for NDEF tag");
            },
            function (error) { // error callback
                alert("Error adding NDEF listener " + JSON.stringify(error));
            }
        );
    },

Edit `config.xml` and `<rim:invoke-target>` just before `</widget>`. (See docs for more info about [invoke-target](https://github.com/chariotsolutions/phonegap-nfc#blackberry-10-invoke-target
).)

    <rim:invoke-target id="your.unique.id.here">
        <type>APPLICATION</type>
        <filter>
            <action>bb.action.OPEN</action>
            <mime-type>application/vnd.rim.nfc.ndef</mime-type>
            <!-- any TNF Empty(0), Well Known(1), MIME Media(2), Absolute URI(3), External(4) -->
            <property var="uris" value="ndef://0,ndef://1,ndef://2,ndef://3,ndef://4" />
        </filter>
    </rim:invoke-target>

Compile, install, and run

    cordova run

![bb10-nfc](https://cloud.githubusercontent.com/assets/3133/10735553/014668f4-7bdf-11e5-9fc3-7d5a8eb95087.png)
