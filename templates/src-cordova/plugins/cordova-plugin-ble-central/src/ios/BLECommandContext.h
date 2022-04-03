//
//  BLECommandContext
//  Holds peripherial, service and characteristic
//

#import <Foundation/Foundation.h>
#import <CoreBluetooth/CoreBluetooth.h>

@interface BLECommandContext : NSObject

@property CBPeripheral *peripheral;
@property CBService *service;
@property CBCharacteristic *characteristic;

@end

