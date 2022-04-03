//
//  BLECentralPlugin.h
//  BLE Central Cordova Plugin
//
//  (c) 2104 Don Coleman
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

#ifndef BLECentralPlugin_h
#define BLECentralPlugin_h

#import <Cordova/CDV.h>
#import <CoreBluetooth/CoreBluetooth.h>
#import "BLECommandContext.h"
#import "CBPeripheral+Extensions.h"

@interface BLECentralPlugin : CDVPlugin <CBCentralManagerDelegate, CBPeripheralDelegate> {
    NSString* discoverPeripheralCallbackId;
    NSString* stateCallbackId;
    NSMutableDictionary* connectCallbacks;
    NSMutableDictionary *readCallbacks;
    NSMutableDictionary *writeCallbacks;
    NSMutableDictionary *notificationCallbacks;
    NSMutableDictionary *startNotificationCallbacks;
    NSMutableDictionary *stopNotificationCallbacks;
    NSMutableDictionary *connectCallbackLatches;
    NSMutableDictionary *readRSSICallbacks;
}

@property (strong, nonatomic) NSMutableSet *peripherals;
@property (strong, nonatomic) CBCentralManager *manager;

- (void)scan:(CDVInvokedUrlCommand *)command;
- (void)startScan:(CDVInvokedUrlCommand *)command;
- (void)startScanWithOptions:(CDVInvokedUrlCommand *)command;
- (void)stopScan:(CDVInvokedUrlCommand *)command;
- (void)connectedPeripheralsWithServices:(CDVInvokedUrlCommand*)command;
- (void)peripheralsWithIdentifiers:(CDVInvokedUrlCommand*)command;

- (void)connect:(CDVInvokedUrlCommand *)command;
- (void)autoConnect:(CDVInvokedUrlCommand *)command;
- (void)disconnect:(CDVInvokedUrlCommand *)command;

- (void)read:(CDVInvokedUrlCommand *)command;
- (void)write:(CDVInvokedUrlCommand *)command;
- (void)writeWithoutResponse:(CDVInvokedUrlCommand *)command;

- (void)startNotification:(CDVInvokedUrlCommand *)command;
- (void)stopNotification:(CDVInvokedUrlCommand *)command;

- (void)isEnabled:(CDVInvokedUrlCommand *)command;
- (void)isConnected:(CDVInvokedUrlCommand *)command;

- (void)startStateNotifications:(CDVInvokedUrlCommand *)command;
- (void)stopStateNotifications:(CDVInvokedUrlCommand *)command;

- (void)onReset;

- (void)readRSSI:(CDVInvokedUrlCommand *)command;

@end

#endif
