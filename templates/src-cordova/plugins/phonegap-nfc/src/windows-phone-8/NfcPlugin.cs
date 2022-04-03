using System.Runtime.Serialization;
using Windows.Networking.Proximity;
using WPCordovaClassLib.Cordova;
using WPCordovaClassLib.Cordova.Commands;
using WPCordovaClassLib.Cordova.JSON;

using System.Runtime.InteropServices.WindowsRuntime;
using Windows.Storage.Streams;
using System.Diagnostics;
using System.IO;

using System.Collections.Generic;
using System.Text;
using System.Collections;

using ChariotSolutions.NFC.NDEF;

// 
// http://www.nfc-forum.org/specs/spec_list/
// http://msdn.microsoft.com/en-us/library/windows/apps/br241250.aspx
// 

namespace Cordova.Extension.Commands
{
    class NfcPlugin : BaseCommand
    {
        private ProximityDevice proximityDevice;
        private long subscribedMessageId = -1;
        private long publishedMessageId = -1;

        public NfcPlugin()
        {
            Debug.WriteLine("Nfc Plugin");
            proximityDevice = ProximityDevice.GetDefault();
            if (proximityDevice == null) // shouldn't happen
            {
                Debug.WriteLine("WARNING: proximity device is null");
            }
        }

        public void init(string args)
        {
            // not used for WP8
        }

        // no args
        public void registerNdef(string args)
        {
            Debug.WriteLine("Registering for NDEF");

            try
            {
                subscribedMessageId = proximityDevice.SubscribeForMessage("NDEF", MessageReceivedHandler);
                DispatchCommandResult(new PluginResult(PluginResult.Status.OK));
            }
            catch (System.Exception e)
            {
                Debug.WriteLine(e);
                DispatchCommandResult(new PluginResult(PluginResult.Status.ERROR, e.Message));
            }
        }

        // no args
        public void removeNdef(string args)
        {
            Debug.WriteLine("Removing NDEF");

            try
            {
                if (subscribedMessageId != -1)
                {
                    proximityDevice.StopSubscribingForMessage(subscribedMessageId);
                    subscribedMessageId = -1;
                }
                DispatchCommandResult(new PluginResult(PluginResult.Status.OK));
            }
            catch (System.Exception e)
            {
                Debug.WriteLine(e);
                DispatchCommandResult(new PluginResult(PluginResult.Status.ERROR, e.Message));
            }

        }

        // args[0] is a NdefMessage, which is a JSON array of NdefRecords
        public void writeTag(string args)
        {
            Debug.WriteLine("Write Tag");

            try
            {
                string ndefMessage = JsonHelper.Deserialize<string[]>(args)[0];
                NdefRecord[] records = JsonHelper.Deserialize<NdefRecord[]>(ndefMessage);
                byte[] data = Ndef.toBytes(records);

                stopPublishing();
                publishedMessageId = proximityDevice.PublishBinaryMessage("NDEF:WriteTag", data.AsBuffer(), nfcWriteTagCallback);

                // send no result now, C# callback will send success after write
                PluginResult result = new PluginResult(PluginResult.Status.NO_RESULT);
                result.KeepCallback = true;
                DispatchCommandResult(result);
            }
            catch (System.Exception e)
            {
                Debug.WriteLine(e);
                DispatchCommandResult(new PluginResult(PluginResult.Status.ERROR, e.Message));
            }
        }

        // args[0] is a NdefMessage, which is a JSON array of NdefRecords
        public void shareTag(string args)
        {
            Debug.WriteLine("Share Tag");

            try
            {
                string ndefMessage = JsonHelper.Deserialize<string[]>(args)[0];
                NdefRecord[] records = JsonHelper.Deserialize<NdefRecord[]>(ndefMessage);
                byte[] data = Ndef.toBytes(records);
            
                stopPublishing();
                publishedMessageId = proximityDevice.PublishBinaryMessage("NDEF", data.AsBuffer());
                DispatchCommandResult(new PluginResult(PluginResult.Status.OK));
            }
            catch (System.Exception e)
            {
                Debug.WriteLine(e);
                DispatchCommandResult(new PluginResult(PluginResult.Status.ERROR, e.Message));
            }
        }

        // no args
        public void unshareTag(string args)
        {
            Debug.WriteLine("Unshare Tag");

            try
            {
                stopPublishing();
                DispatchCommandResult(new PluginResult(PluginResult.Status.OK));
            }
            catch (System.Exception e)
            {
                Debug.WriteLine(e);
                DispatchCommandResult(new PluginResult(PluginResult.Status.ERROR, e.Message));
            }
        }

        private void stopPublishing()
        {
            if (publishedMessageId != -1)
            {
                proximityDevice.StopPublishingMessage(publishedMessageId);
                publishedMessageId = -1;
            }
        }

        // MessageTransmittedHandler called after the message is written to a tag
        private void nfcWriteTagCallback(ProximityDevice sender, long messageId)
        {
            Debug.WriteLine("Successfully wrote message to the NFC tag.");

            // only write the tag one time
            stopPublishing();

            DispatchCommandResult(new PluginResult(PluginResult.Status.OK));
        }

        private void MessageReceivedHandler(ProximityDevice sender, ProximityMessage message)
        {

            var bytes = message.Data.ToArray();
            List<NdefRecord> records = Ndef.parse(bytes);

            NfcTag tag = new NfcTag(records);

           // calling a global js method to fire an nfc event
           ScriptCallback script = new ScriptCallback("fireNfcTagEvent", new string[] { "ndef", JsonHelper.Serialize(tag) });
           this.InvokeCustomScript(script, false);
        }

        [DataContract]
        public class NfcTag
        {
            public NfcTag()
            {
            }

            public NfcTag(List<NdefRecord> records)
            {
                ndefMessage = records;
            }

            [DataMember]
            public List<NdefRecord> ndefMessage { get; set; }
        }

    }
}
