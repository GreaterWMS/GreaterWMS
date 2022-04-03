//
//  CBPeripheral+Extensions.m
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

#import "CBPeripheral+Extensions.h"

static char ADVERTISING_IDENTIFER;
static char SAVED_RSSI_IDENTIFER;

static NSDictionary *dataToArrayBuffer(NSData* data) {
    return @{
             @"CDVType" : @"ArrayBuffer",
             @"data" :[data base64EncodedStringWithOptions:0]
             };
}

@implementation CBPeripheral(com_megster_ble_extension)

-(NSString *)uuidAsString {
    if (self.identifier.UUIDString) {
        return self.identifier.UUIDString;
    } else {
        return @"";
    }
}


-(NSDictionary *)asDictionary {
    NSString *uuidString = NULL;
    if (self.identifier.UUIDString) {
        uuidString = self.identifier.UUIDString;
    } else {
        uuidString = @"";
    }

    NSMutableDictionary *dictionary = [NSMutableDictionary dictionary];
    [dictionary setObject: uuidString forKey: @"id"];

    if ([self name]) {
        [dictionary setObject: [self name] forKey: @"name"];
    }

    if ([self savedRSSI]) {
        [dictionary setObject: [self savedRSSI] forKey: @"rssi"];
    }

    if ([self advertising]) {
        [dictionary setObject: [self advertising] forKey: @"advertising"];
    }

    if([[self services] count] > 0) {
        [self serviceAndCharacteristicInfo: dictionary];
    }

    return dictionary;
}

// AdvertisementData is from didDiscoverPeripheral. RFduino advertises a service name in the Mfg Data Field.
-(void)setAdvertisementData:(NSDictionary *)advertisementData RSSI:(NSNumber *)rssi {
    [self setAdvertising:[self serializableAdvertisementData: advertisementData]];
    [self setSavedRSSI: rssi];
}

// Translates the Advertisement Data from didDiscoverPeripheral into a structure that can be serialized as JSON
//
// This version keeps the iOS constants for keys, future versions could create more friendly keys
// https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/advertisement_data_retrieval_keys?language=objc
//
// Advertisement Data from a Peripheral could look something like
//
// advertising = {
//     kCBAdvDataChannel = 39;
//     kCBAdvDataIsConnectable = 1;
//     kCBAdvDataLocalName = foo;
//     kCBAdvDataManufacturerData = {
//         CDVType = ArrayBuffer;
//         data = "AABoZWxsbw==";
//     };
//     kCBAdvDataServiceData = {
//         FED8 = {
//             CDVType = ArrayBuffer;
//             data = "ACAAYWJjBw==";
//         };
//     };
//     kCBAdvDataServiceUUIDs = (
//         FED8
//     );
//     kCBAdvDataTxPowerLevel = 32;
//};
- (NSDictionary *) serializableAdvertisementData: (NSDictionary *) advertisementData {
    NSMutableDictionary *result = [NSMutableDictionary dictionary];

    NSString *localName = [advertisementData objectForKey:CBAdvertisementDataLocalNameKey];
    if (localName) {
        [result setObject:localName forKey:CBAdvertisementDataLocalNameKey];
    }

    NSNumber *txPowerLevel = [advertisementData objectForKey:CBAdvertisementDataTxPowerLevelKey];
    if (txPowerLevel) {
        [result setObject:txPowerLevel forKey:CBAdvertisementDataTxPowerLevelKey];
    }

    NSNumber *isConnectable = [advertisementData objectForKey:CBAdvertisementDataIsConnectable];
    if (isConnectable) {
        [result setObject:isConnectable forKey:CBAdvertisementDataIsConnectable];
    }

    // Convert the manufacturer data
    NSData *mfgData = [advertisementData objectForKey:CBAdvertisementDataManufacturerDataKey];
    if (mfgData) {
        [result setObject:dataToArrayBuffer([advertisementData objectForKey:CBAdvertisementDataManufacturerDataKey]) forKey:CBAdvertisementDataManufacturerDataKey];
    }

    // Service Data is a dictionary of CBUUID and NSData
    // Convert to String keys with Array Buffer values
    NSMutableDictionary *serviceData = [advertisementData objectForKey:CBAdvertisementDataServiceDataKey];
    if (serviceData) {
        NSLog(@"%@", serviceData);

        for (CBUUID *key in [serviceData allKeys]) {
            [serviceData setObject:dataToArrayBuffer([serviceData objectForKey:key]) forKey:[key UUIDString]];
            [serviceData removeObjectForKey:key];
        }

        [result setObject:serviceData forKey:CBAdvertisementDataServiceDataKey];
    }

    // Create a new list of Service UUIDs as Strings instead of CBUUIDs
    NSMutableArray *serviceUUIDs = [advertisementData objectForKey:CBAdvertisementDataServiceUUIDsKey];
    NSMutableArray *serviceUUIDStrings;
    if (serviceUUIDs) {
        serviceUUIDStrings = [[NSMutableArray alloc] initWithCapacity:serviceUUIDs.count];

        for (CBUUID *uuid in serviceUUIDs) {
            [serviceUUIDStrings addObject:[uuid UUIDString]];
        }

        // replace the UUID list with list of strings
        [result setObject:serviceUUIDStrings forKey:CBAdvertisementDataServiceUUIDsKey];
    }

    // Solicited Services UUIDs is an array of CBUUIDs, convert into Strings
    NSMutableArray *solicitiedServiceUUIDs = [advertisementData objectForKey:CBAdvertisementDataSolicitedServiceUUIDsKey];
    NSMutableArray *solicitiedServiceUUIDStrings;
    if (solicitiedServiceUUIDs) {
        // NSLog(@"%@", solicitiedServiceUUIDs);
        solicitiedServiceUUIDStrings = [[NSMutableArray alloc] initWithCapacity:solicitiedServiceUUIDs.count];

        for (CBUUID *uuid in solicitiedServiceUUIDs) {
            [solicitiedServiceUUIDStrings addObject:[uuid UUIDString]];
        }

        // replace the UUID list with list of strings
        [result setObject:solicitiedServiceUUIDStrings forKey:CBAdvertisementDataSolicitedServiceUUIDsKey];
    }
    
    // Undocumented kCBAdvDataLeBluetoothDeviceAddress which contains MAC address see
    // 0x1B «LE Bluetooth Device Address» Core Specification Supplement, Part A, section 1.16
    NSData *bluetoothDeviceAddress = [advertisementData objectForKey:@"kCBAdvDataLeBluetoothDeviceAddress"];
    if (bluetoothDeviceAddress) {
        [result setObject:dataToArrayBuffer(bluetoothDeviceAddress) forKey:@"kCBAdvDataLeBluetoothDeviceAddress"];
    }

    return result;
}

// Put the service, characteristic, and descriptor data in a format that will serialize through JSON
// sending a list of services and a list of characteristics
- (void) serviceAndCharacteristicInfo: (NSMutableDictionary *) info {
    NSMutableArray *serviceList = [NSMutableArray new];
    NSMutableArray *characteristicList = [NSMutableArray new];

    // This can move into the CBPeripherial Extension
    for (CBService *service in [self services]) {
        [serviceList addObject:[[service UUID] UUIDString]];
        for (CBCharacteristic *characteristic in service.characteristics) {
            NSMutableDictionary *characteristicDictionary = [NSMutableDictionary new];
            [characteristicDictionary setObject:[[service UUID] UUIDString] forKey:@"service"];
            [characteristicDictionary setObject:[[characteristic UUID] UUIDString] forKey:@"characteristic"];

            if ([characteristic value]) {
                [characteristicDictionary setObject:dataToArrayBuffer([characteristic value]) forKey:@"value"];
            }
            if ([characteristic properties]) {
                //[characteristicDictionary setObject:[NSNumber numberWithInt:[characteristic properties]] forKey:@"propertiesValue"];
                [characteristicDictionary setObject:[self decodeCharacteristicProperties:characteristic] forKey:@"properties"];
            }
            // permissions only exist on CBMutableCharacteristics
            [characteristicDictionary setObject:[NSNumber numberWithBool:[characteristic isNotifying]] forKey:@"isNotifying"];
            [characteristicList addObject:characteristicDictionary];

            // descriptors always seem to be nil, probably a bug here
            NSMutableArray *descriptorList = [NSMutableArray new];
            for (CBDescriptor *descriptor in characteristic.descriptors) {
                NSMutableDictionary *descriptorDictionary = [NSMutableDictionary new];
                [descriptorDictionary setObject:[[descriptor UUID] UUIDString] forKey:@"descriptor"];
                if ([descriptor value]) { // should always have a value?
                    [descriptorDictionary setObject:[descriptor value] forKey:@"value"];
                }
                [descriptorList addObject:descriptorDictionary];
            }
            if ([descriptorList count] > 0) {
                [characteristicDictionary setObject:descriptorList forKey:@"descriptors"];
            }

        }
    }

    [info setObject:serviceList forKey:@"services"];
    [info setObject:characteristicList forKey:@"characteristics"];
}

-(NSArray *) decodeCharacteristicProperties: (CBCharacteristic *) characteristic {
    NSMutableArray *props = [NSMutableArray new];

    CBCharacteristicProperties p = [characteristic properties];

    // NOTE: props strings need to be consistent across iOS and Android
    if ((p & CBCharacteristicPropertyBroadcast) != 0x0) {
        [props addObject:@"Broadcast"];
    }

    if ((p & CBCharacteristicPropertyRead) != 0x0) {
        [props addObject:@"Read"];
    }

    if ((p & CBCharacteristicPropertyWriteWithoutResponse) != 0x0) {
        [props addObject:@"WriteWithoutResponse"];
    }

    if ((p & CBCharacteristicPropertyWrite) != 0x0) {
        [props addObject:@"Write"];
    }

    if ((p & CBCharacteristicPropertyNotify) != 0x0) {
        [props addObject:@"Notify"];
    }

    if ((p & CBCharacteristicPropertyIndicate) != 0x0) {
        [props addObject:@"Indicate"];
    }

    if ((p & CBCharacteristicPropertyAuthenticatedSignedWrites) != 0x0) {
        [props addObject:@"AutheticateSignedWrites"];
    }

    if ((p & CBCharacteristicPropertyExtendedProperties) != 0x0) {
        [props addObject:@"ExtendedProperties"];
    }

    if ((p & CBCharacteristicPropertyNotifyEncryptionRequired) != 0x0) {
        [props addObject:@"NotifyEncryptionRequired"];
    }

    if ((p & CBCharacteristicPropertyIndicateEncryptionRequired) != 0x0) {
        [props addObject:@"IndicateEncryptionRequired"];
    }

    return props;
}

-(void)setAdvertising:(NSDictionary *)newAdvertisingValue{
    objc_setAssociatedObject(self, &ADVERTISING_IDENTIFER, newAdvertisingValue, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
}

-(NSString*)advertising{
    return objc_getAssociatedObject(self, &ADVERTISING_IDENTIFER);
}


-(void)setSavedRSSI:(NSNumber *)newSavedRSSIValue {
    objc_setAssociatedObject(self, &SAVED_RSSI_IDENTIFER, newSavedRSSIValue, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
}

-(NSString*)savedRSSI{
    return objc_getAssociatedObject(self, &SAVED_RSSI_IDENTIFER);
}

@end
