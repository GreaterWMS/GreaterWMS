//
//  BLE Central Cordova Plugin
//
//  (c) 2105 Don Coleman
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

using System;
using System.Linq;
using System.Collections.Generic;
using System.Diagnostics;
using System.Runtime.Serialization;
using Windows.Networking.Proximity;
using WPCordovaClassLib.Cordova;
using WPCordovaClassLib.Cordova.Commands;
using WPCordovaClassLib.Cordova.JSON;
using Microsoft.Phone.Tasks;

using Windows.Networking;
using System.Text;
using System.Threading;

public class BLECentralPlugin : BaseCommand
{

    private void notImplemented()
    {
      DispatchCommandResult(new PluginResult(PluginResult.Status.ERROR, "Not Implemented"));
    }

    public void scan(string args)
    {
      notImplemented();
    }
    public void startScan(string args)
    {
      notImplemented();
    }
    public void stopScan(string args)
    {
      notImplemented();
    }
    public void startScanWithOptions(string args)
    {
      notImplemented();
    }
    public void connect(string args)
    {
      notImplemented();
    }
    public void disconnect(string args)
    {
      notImplemented();
    }
    public void read(string args)
    {
      notImplemented();
    }
    public void readRSSI(string args) 
    {
      notImplemented();
    }
    public void write(string args)
    {
      notImplemented();
    }
    public void writeWithoutResponse(string args)
    {
      notImplemented();
    }
    public void startNotification(string args)
    {
      notImplemented();
    }
    public void stopNotification(string args)
    {
      notImplemented();
    }
    public void isConnected(string args)
    {
      notImplemented();
    }

    public async void isEnabled(string args)
    {
        string callbackId = JsonHelper.Deserialize<string[]>(args)[0];

        // This is a bad way to do this, improve later
        // See if we can determine in the Connection Manager
        // https://msdn.microsoft.com/library/windows/apps/jj207007(v=vs.105).aspx
        PeerFinder.AlternateIdentities["Bluetooth:Paired"] = "";

        try
        {
            var peers = await PeerFinder.FindAllPeersAsync();

            // Handle the result of the FindAllPeersAsync call
        }
        catch (Exception ex)
        {
            if ((uint)ex.HResult == 0x8007048F)
            {
                DispatchCommandResult(new PluginResult(PluginResult.Status.ERROR), callbackId);
            }
            else
            {
                DispatchCommandResult(new PluginResult(PluginResult.Status.ERROR, ex.Message), callbackId);
            }
        }

        DispatchCommandResult(new PluginResult(PluginResult.Status.OK), callbackId);
    }

    public void showBluetoothSettings(string args)
    {
        ConnectionSettingsTask connectionSettingsTask = new ConnectionSettingsTask();
        connectionSettingsTask.ConnectionSettingsType = ConnectionSettingsType.Bluetooth;
        connectionSettingsTask.Show();
        DispatchCommandResult(new PluginResult(PluginResult.Status.OK));
    }

}
