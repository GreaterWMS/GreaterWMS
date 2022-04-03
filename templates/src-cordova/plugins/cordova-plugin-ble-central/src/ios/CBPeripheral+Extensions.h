//
//  CBPeripheral+Extensions.h
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

#import <objc/runtime.h>
#import <Foundation/Foundation.h>
#import <CoreBluetooth/CoreBluetooth.h>
#import <Cordova/CDV.h>


@interface CBPeripheral(com_megster_ble_extension)

@property (nonatomic, retain) NSDictionary *advertising;
@property (nonatomic, retain) NSNumber *savedRSSI;

-(void)setAdvertisementData:(NSDictionary *)advertisementData RSSI:(NSNumber*)rssi;
-(NSDictionary *)asDictionary;
-(NSString *)uuidAsString;

@end



