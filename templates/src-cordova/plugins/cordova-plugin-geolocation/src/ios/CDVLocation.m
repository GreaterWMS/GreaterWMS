/*
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache License, Version 2.0 (the
 "License"); you may not use this file except in compliance
 with the License.  You may obtain a copy of the License at
 
 http://www.apache.org/licenses/LICENSE-2.0
 
 Unless required by applicable law or agreed to in writing,
 software distributed under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the License for the
 specific language governing permissions and limitations
 under the License.
 */

#import "CDVLocation.h"

#pragma mark Constants

#define kPGLocationErrorDomain @"kPGLocationErrorDomain"
#define kPGLocationDesiredAccuracyKey @"desiredAccuracy"
#define kPGLocationForcePromptKey @"forcePrompt"
#define kPGLocationDistanceFilterKey @"distanceFilter"
#define kPGLocationFrequencyKey @"frequency"

#pragma mark -
#pragma mark Categories

@implementation CDVLocationData

@synthesize locationStatus, locationInfo, locationCallbacks, watchCallbacks;
- (CDVLocationData*)init
{
    self = (CDVLocationData*)[super init];
    if (self) {
        self.locationInfo = nil;
        self.locationCallbacks = nil;
        self.watchCallbacks = nil;
    }
    return self;
}

@end

#pragma mark -
#pragma mark CDVLocation

@implementation CDVLocation

@synthesize locationManager, locationData;

- (void)pluginInitialize
{
    self.locationManager = [[CLLocationManager alloc] init];
    self.locationManager.delegate = self; // Tells the location manager to send updates to this object
    __locationStarted = NO;
    __highAccuracyEnabled = NO;
    self.locationData = nil;
}

- (BOOL)isAuthorized
{
    BOOL authorizationStatusClassPropertyAvailable = [CLLocationManager respondsToSelector:@selector(authorizationStatus)]; // iOS 4.2+
    
    if (authorizationStatusClassPropertyAvailable) {
        NSUInteger authStatus = [CLLocationManager authorizationStatus];
#ifdef __IPHONE_8_0
        if ([self.locationManager respondsToSelector:@selector(requestWhenInUseAuthorization)]) {  //iOS 8.0+
            return (authStatus == kCLAuthorizationStatusAuthorizedWhenInUse) || (authStatus == kCLAuthorizationStatusAuthorizedAlways) || (authStatus == kCLAuthorizationStatusNotDetermined);
        }
#endif
        return (authStatus == kCLAuthorizationStatusAuthorizedAlways) || (authStatus == kCLAuthorizationStatusNotDetermined);
    }
    
    // by default, assume YES (for iOS < 4.2)
    return YES;
}

- (BOOL)isLocationServicesEnabled
{
    BOOL locationServicesEnabledInstancePropertyAvailable = [self.locationManager respondsToSelector:@selector(locationServicesEnabled)]; // iOS 3.x
    BOOL locationServicesEnabledClassPropertyAvailable = [CLLocationManager respondsToSelector:@selector(locationServicesEnabled)]; // iOS 4.x
    
    if (locationServicesEnabledClassPropertyAvailable) { // iOS 4.x
        return [CLLocationManager locationServicesEnabled];
    } else {
        return NO;
    }
}

- (void)startLocation:(BOOL)enableHighAccuracy
{
    if (![self isLocationServicesEnabled]) {
        [self returnLocationError:PERMISSIONDENIED withMessage:@"Location services are not enabled."];
        return;
    }
    if (![self isAuthorized]) {
        NSString* message = nil;
        BOOL authStatusAvailable = [CLLocationManager respondsToSelector:@selector(authorizationStatus)]; // iOS 4.2+
        if (authStatusAvailable) {
            NSUInteger code = [CLLocationManager authorizationStatus];
            if (code == kCLAuthorizationStatusNotDetermined) {
                // could return POSITION_UNAVAILABLE but need to coordinate with other platforms
                message = @"User undecided on application's use of location services.";
            } else if (code == kCLAuthorizationStatusRestricted) {
                message = @"Application's use of location services is restricted.";
            }
        }
        // PERMISSIONDENIED is only PositionError that makes sense when authorization denied
        [self returnLocationError:PERMISSIONDENIED withMessage:message];
        
        return;
    }
    
#ifdef __IPHONE_8_0
    NSUInteger code = [CLLocationManager authorizationStatus];
    if (code == kCLAuthorizationStatusNotDetermined && ([self.locationManager respondsToSelector:@selector(requestAlwaysAuthorization)] || [self.locationManager respondsToSelector:@selector(requestWhenInUseAuthorization)])) { //iOS8+
        __highAccuracyEnabled = enableHighAccuracy;
        if([[NSBundle mainBundle] objectForInfoDictionaryKey:@"NSLocationWhenInUseUsageDescription"]){
            [self.locationManager requestWhenInUseAuthorization];
        } else if([[NSBundle mainBundle] objectForInfoDictionaryKey:@"NSLocationAlwaysUsageDescription"]) {
            [self.locationManager  requestAlwaysAuthorization];
        } else {
            NSLog(@"[Warning] No NSLocationAlwaysUsageDescription or NSLocationWhenInUseUsageDescription key is defined in the Info.plist file.");
        }
        return;
    }
#endif
    
    // Tell the location manager to start notifying us of location updates. We
    // first stop, and then start the updating to ensure we get at least one
    // update, even if our location did not change.
    [self.locationManager stopUpdatingLocation];
    [self.locationManager startUpdatingLocation];
    __locationStarted = YES;
    if (enableHighAccuracy) {
        __highAccuracyEnabled = YES;
        // Set distance filter to 5 for a high accuracy. Setting it to "kCLDistanceFilterNone" could provide a
        // higher accuracy, but it's also just spamming the callback with useless reports which drain the battery.
        self.locationManager.distanceFilter = 5;
        // Set desired accuracy to Best.
        self.locationManager.desiredAccuracy = kCLLocationAccuracyBest;
    } else {
        __highAccuracyEnabled = NO;
        self.locationManager.distanceFilter = 10;
        self.locationManager.desiredAccuracy = kCLLocationAccuracyThreeKilometers;
    }
}

- (void)_stopLocation
{
    if (__locationStarted) {
        if (![self isLocationServicesEnabled]) {
            return;
        }
        
        [self.locationManager stopUpdatingLocation];
        __locationStarted = NO;
        __highAccuracyEnabled = NO;
    }
}

- (void)locationManager:(CLLocationManager*)manager
    didUpdateToLocation:(CLLocation*)newLocation
           fromLocation:(CLLocation*)oldLocation
{
    CDVLocationData* cData = self.locationData;
    
    cData.locationInfo = newLocation;
    @synchronized (self.locationData.locationCallbacks) {
        if (self.locationData.locationCallbacks.count > 0) {
            for (NSString* callbackId in self.locationData.locationCallbacks) {
                [self returnLocationInfo:callbackId andKeepCallback:NO];
            }
            
            [self.locationData.locationCallbacks removeAllObjects];
        }
    }
    if (self.locationData.watchCallbacks.count > 0) {
        for (NSString* timerId in self.locationData.watchCallbacks) {
            [self returnLocationInfo:[self.locationData.watchCallbacks objectForKey:timerId] andKeepCallback:YES];
        }
    } else {
        // No callbacks waiting on us anymore, turn off listening.
        [self _stopLocation];
    }
}

- (void)getLocation:(CDVInvokedUrlCommand*)command
{
    [self.commandDelegate runInBackground:^{
        NSString* callbackId = command.callbackId;
        BOOL enableHighAccuracy = [[command argumentAtIndex:0] boolValue];
        
        if ([self isLocationServicesEnabled] == NO) {
            NSMutableDictionary* posError = [NSMutableDictionary dictionaryWithCapacity:2];
            [posError setObject:[NSNumber numberWithInt:PERMISSIONDENIED] forKey:@"code"];
            [posError setObject:@"Location services are disabled." forKey:@"message"];
            CDVPluginResult* result = [CDVPluginResult resultWithStatus:CDVCommandStatus_ERROR messageAsDictionary:posError];
            [self.commandDelegate sendPluginResult:result callbackId:callbackId];
        } else {
            if (!self.locationData) {
                self.locationData = [[CDVLocationData alloc] init];
            }
            CDVLocationData* lData = self.locationData;
            @synchronized (self.locationData.locationCallbacks) {
                if (!lData.locationCallbacks) {
                    lData.locationCallbacks = [NSMutableArray arrayWithCapacity:1];
                }
            }
            
            if (!__locationStarted || (__highAccuracyEnabled != enableHighAccuracy)) {
                // add the callbackId into the array so we can call back when get data
                @synchronized (self.locationData.locationCallbacks) {
                    if (callbackId != nil) {
                        [lData.locationCallbacks addObject:callbackId];
                    }
                }
                // Tell the location manager to start notifying us of heading updates
                [self startLocation:enableHighAccuracy];
            } else {
                [self returnLocationInfo:callbackId andKeepCallback:NO];
            }
        }
    }];
}

- (void)addWatch:(CDVInvokedUrlCommand*)command
{
    NSString* callbackId = command.callbackId;
    NSString* timerId = [command argumentAtIndex:0];
    BOOL enableHighAccuracy = [[command argumentAtIndex:1] boolValue];
    
    if (!self.locationData) {
        self.locationData = [[CDVLocationData alloc] init];
    }
    CDVLocationData* lData = self.locationData;
    
    if (!lData.watchCallbacks) {
        lData.watchCallbacks = [NSMutableDictionary dictionaryWithCapacity:1];
    }
    
    // add the callbackId into the dictionary so we can call back whenever get data
    [lData.watchCallbacks setObject:callbackId forKey:timerId];
    
    if ([self isLocationServicesEnabled] == NO) {
        NSMutableDictionary* posError = [NSMutableDictionary dictionaryWithCapacity:2];
        [posError setObject:[NSNumber numberWithInt:PERMISSIONDENIED] forKey:@"code"];
        [posError setObject:@"Location services are disabled." forKey:@"message"];
        CDVPluginResult* result = [CDVPluginResult resultWithStatus:CDVCommandStatus_ERROR messageAsDictionary:posError];
        [self.commandDelegate sendPluginResult:result callbackId:callbackId];
    } else {
        if (!__locationStarted || (__highAccuracyEnabled != enableHighAccuracy)) {
            // Tell the location manager to start notifying us of location updates
            [self startLocation:enableHighAccuracy];
        }
    }
}

- (void)clearWatch:(CDVInvokedUrlCommand*)command
{
    NSString* timerId = [command argumentAtIndex:0];
    
    if (self.locationData && self.locationData.watchCallbacks && [self.locationData.watchCallbacks objectForKey:timerId]) {
        [self.locationData.watchCallbacks removeObjectForKey:timerId];
        if([self.locationData.watchCallbacks count] == 0) {
            [self _stopLocation];
        }
    }
}

- (void)stopLocation:(CDVInvokedUrlCommand*)command
{
    [self _stopLocation];
}

- (void)returnLocationInfo:(NSString*)callbackId andKeepCallback:(BOOL)keepCallback
{
    CDVPluginResult* result = nil;
    CDVLocationData* lData = self.locationData;
    
    if (lData && !lData.locationInfo) {
        // return error
        result = [CDVPluginResult resultWithStatus:CDVCommandStatus_ERROR messageToErrorObject:POSITIONUNAVAILABLE];
    } else if (lData && lData.locationInfo) {
        CLLocation* lInfo = lData.locationInfo;
        NSMutableDictionary* returnInfo = [NSMutableDictionary dictionaryWithCapacity:8];
        NSNumber* timestamp = [NSNumber numberWithDouble:([lInfo.timestamp timeIntervalSince1970] * 1000)];
        [returnInfo setObject:timestamp forKey:@"timestamp"];
        [returnInfo setObject:[NSNumber numberWithDouble:lInfo.speed] forKey:@"velocity"];
        [returnInfo setObject:[NSNumber numberWithDouble:lInfo.verticalAccuracy] forKey:@"altitudeAccuracy"];
        [returnInfo setObject:[NSNumber numberWithDouble:lInfo.horizontalAccuracy] forKey:@"accuracy"];
        [returnInfo setObject:[NSNumber numberWithDouble:lInfo.course] forKey:@"heading"];
        [returnInfo setObject:[NSNumber numberWithDouble:lInfo.altitude] forKey:@"altitude"];
        [returnInfo setObject:[NSNumber numberWithDouble:lInfo.coordinate.latitude] forKey:@"latitude"];
        [returnInfo setObject:[NSNumber numberWithDouble:lInfo.coordinate.longitude] forKey:@"longitude"];
        
        result = [CDVPluginResult resultWithStatus:CDVCommandStatus_OK messageAsDictionary:returnInfo];
        [result setKeepCallbackAsBool:keepCallback];
    }
    if (result) {
        [self.commandDelegate sendPluginResult:result callbackId:callbackId];
    }
}

- (void)returnLocationError:(NSUInteger)errorCode withMessage:(NSString*)message
{
    NSMutableDictionary* posError = [NSMutableDictionary dictionaryWithCapacity:2];
    
    [posError setObject:[NSNumber numberWithUnsignedInteger:errorCode] forKey:@"code"];
    [posError setObject:message ? message:@"" forKey:@"message"];
    CDVPluginResult* result = [CDVPluginResult resultWithStatus:CDVCommandStatus_ERROR messageAsDictionary:posError];
    
    
    @synchronized (self.locationData.locationCallbacks) {
        for (NSString* callbackId in self.locationData.locationCallbacks) {
            [self.commandDelegate sendPluginResult:result callbackId:callbackId];
        }
        
        [self.locationData.locationCallbacks removeAllObjects];
    }
    
    for (NSString* callbackId in self.locationData.watchCallbacks) {
        [self.commandDelegate sendPluginResult:result callbackId:callbackId];
    }
}

- (void)locationManager:(CLLocationManager*)manager didFailWithError:(NSError*)error
{
    NSLog(@"locationManager::didFailWithError %@", [error localizedFailureReason]);
    
    CDVLocationData* lData = self.locationData;
    if (lData && __locationStarted) {
        // TODO: probably have to once over the various error codes and return one of:
        // PositionError.PERMISSION_DENIED = 1;
        // PositionError.POSITION_UNAVAILABLE = 2;
        // PositionError.TIMEOUT = 3;
        NSUInteger positionError = POSITIONUNAVAILABLE;
        if (error.code == kCLErrorDenied) {
            positionError = PERMISSIONDENIED;
        }
        [self returnLocationError:positionError withMessage:[error localizedDescription]];
    }
    
    if (error.code != kCLErrorLocationUnknown) {
        [self.locationManager stopUpdatingLocation];
        __locationStarted = NO;
    }
}

//iOS8+
-(void)locationManager:(CLLocationManager *)manager didChangeAuthorizationStatus:(CLAuthorizationStatus)status
{
    if(!__locationStarted){
        [self startLocation:__highAccuracyEnabled];
    }
}

- (void)dealloc
{
    self.locationManager.delegate = nil;
}

- (void)onReset
{
    [self _stopLocation];
    [self.locationManager stopUpdatingHeading];
}

@end
