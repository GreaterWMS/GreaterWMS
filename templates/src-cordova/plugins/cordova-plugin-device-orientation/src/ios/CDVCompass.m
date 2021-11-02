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

#import "CDVCompass.h"

#pragma mark Constants

#define kPGLocationErrorDomain @"kPGLocationErrorDomain"
#define kPGLocationDesiredAccuracyKey @"desiredAccuracy"
#define kPGLocationForcePromptKey @"forcePrompt"
#define kPGLocationDistanceFilterKey @"distanceFilter"
#define kPGLocationFrequencyKey @"frequency"

#pragma mark -
#pragma mark CDVHeadingData

@implementation CDVHeadingData

@synthesize headingStatus, headingInfo, headingCallbacks, headingFilter, headingTimestamp, timeout;
- (CDVHeadingData*)init
{
    self = (CDVHeadingData*)[super init];
    if (self) {
        self.headingStatus = HEADINGSTOPPED;
        self.headingInfo = nil;
        self.headingCallbacks = nil;
        self.headingFilter = nil;
        self.headingTimestamp = nil;
        self.timeout = 10;
    }
    return self;
}

@end

#pragma mark -
#pragma mark CDVLocation

@implementation CDVCompass

@synthesize locationManager, headingData;

- (void)pluginInitialize
{
    self.locationManager = [[CLLocationManager alloc] init];
    self.locationManager.delegate = self; // Tells the location manager to send updates to this object
    __locationStarted = NO;
    __highAccuracyEnabled = NO;
    self.headingData = nil;
}

- (BOOL)hasHeadingSupport
{
    BOOL headingInstancePropertyAvailable = [self.locationManager respondsToSelector:@selector(headingAvailable)]; // iOS 3.x
    BOOL headingClassPropertyAvailable = [CLLocationManager respondsToSelector:@selector(headingAvailable)]; // iOS 4.x

    if (headingInstancePropertyAvailable) { // iOS 3.x
        return [(id)self.locationManager headingAvailable];
    } else if (headingClassPropertyAvailable) { // iOS 4.x
        return [CLLocationManager headingAvailable];
    } else { // iOS 2.x
        return NO;
    }
}

// called to get the current heading
// Will call location manager to startUpdatingHeading if necessary

- (void)getHeading:(CDVInvokedUrlCommand*)command
{
    NSString* callbackId = command.callbackId;
    NSDictionary* options = [command argumentAtIndex:0 withDefault:nil];
    NSNumber* filter = [options valueForKey:@"filter"];

    if (filter) {
        [self watchHeadingFilter:command];
        return;
    }
    if ([self hasHeadingSupport] == NO) {
        CDVPluginResult* result = [CDVPluginResult resultWithStatus:CDVCommandStatus_ERROR messageAsInt:20];
        [self.commandDelegate sendPluginResult:result callbackId:callbackId];
    } else {
        // heading retrieval does is not affected by disabling locationServices and authorization of app for location services
        if (!self.headingData) {
            self.headingData = [[CDVHeadingData alloc] init];
        }
        CDVHeadingData* hData = self.headingData;

        if (!hData.headingCallbacks) {
            hData.headingCallbacks = [NSMutableArray arrayWithCapacity:1];
        }
        // add the callbackId into the array so we can call back when get data
        [hData.headingCallbacks addObject:callbackId];

        if ((hData.headingStatus != HEADINGRUNNING) && (hData.headingStatus != HEADINGERROR)) {
            // Tell the location manager to start notifying us of heading updates
            [self startHeadingWithFilter:0.2];
        } else {
            [self returnHeadingInfo:callbackId keepCallback:NO];
        }
    }
}

// called to request heading updates when heading changes by a certain amount (filter)
- (void)watchHeadingFilter:(CDVInvokedUrlCommand*)command
{
    NSString* callbackId = command.callbackId;
    NSDictionary* options = [command argumentAtIndex:0 withDefault:nil];
    NSNumber* filter = [options valueForKey:@"filter"];
    CDVHeadingData* hData = self.headingData;

    if ([self hasHeadingSupport] == NO) {
        CDVPluginResult* result = [CDVPluginResult resultWithStatus:CDVCommandStatus_ERROR messageAsInt:20];
        [self.commandDelegate sendPluginResult:result callbackId:callbackId];
    } else {
        if (!hData) {
            self.headingData = [[CDVHeadingData alloc] init];
            hData = self.headingData;
        }
        if (hData.headingStatus != HEADINGRUNNING) {
            // Tell the location manager to start notifying us of heading updates
            [self startHeadingWithFilter:[filter doubleValue]];
        } else {
            // if already running check to see if due to existing watch filter
            if (hData.headingFilter && ![hData.headingFilter isEqualToString:callbackId]) {
                // new watch filter being specified
                // send heading data one last time to clear old successCallback
                [self returnHeadingInfo:hData.headingFilter keepCallback:NO];
            }
        }
        // save the new filter callback and update the headingFilter setting
        hData.headingFilter = callbackId;
        // check if need to stop and restart in order to change value???
        self.locationManager.headingFilter = [filter doubleValue];
    }
}

- (void)returnHeadingInfo:(NSString*)callbackId keepCallback:(BOOL)bRetain
{
    CDVPluginResult* result = nil;
    CDVHeadingData* hData = self.headingData;

    self.headingData.headingTimestamp = [NSDate date];

    if (hData && (hData.headingStatus == HEADINGERROR)) {
        // return error
        result = [CDVPluginResult resultWithStatus:CDVCommandStatus_ERROR messageAsInt:0];
    } else if (hData && (hData.headingStatus == HEADINGRUNNING) && hData.headingInfo) {
        // if there is heading info, return it
        CLHeading* hInfo = hData.headingInfo;
        NSMutableDictionary* returnInfo = [NSMutableDictionary dictionaryWithCapacity:4];
        NSNumber* timestamp = [NSNumber numberWithDouble:([hInfo.timestamp timeIntervalSince1970] * 1000)];
        [returnInfo setObject:timestamp forKey:@"timestamp"];
        [returnInfo setObject:[NSNumber numberWithDouble:hInfo.magneticHeading] forKey:@"magneticHeading"];
        id trueHeading = __locationStarted ? (id)[NSNumber numberWithDouble : hInfo.trueHeading] : (id)[NSNull null];
        [returnInfo setObject:trueHeading forKey:@"trueHeading"];
        [returnInfo setObject:[NSNumber numberWithDouble:hInfo.headingAccuracy] forKey:@"headingAccuracy"];

        result = [CDVPluginResult resultWithStatus:CDVCommandStatus_OK messageAsDictionary:returnInfo];
        [result setKeepCallbackAsBool:bRetain];
    }
    if (result) {
        [self.commandDelegate sendPluginResult:result callbackId:callbackId];
    }
}

- (void)stopHeading:(CDVInvokedUrlCommand*)command
{
    // CDVHeadingData* hData = self.headingData;
    if (self.headingData && (self.headingData.headingStatus != HEADINGSTOPPED)) {
        if (self.headingData.headingFilter) {
            // callback one last time to clear callback
            [self returnHeadingInfo:self.headingData.headingFilter keepCallback:NO];
            self.headingData.headingFilter = nil;
        }
        [self.locationManager stopUpdatingHeading];
        NSLog(@"heading STOPPED");
        self.headingData = nil;
    }
}

// helper method to check the orientation and start updating headings
- (void)startHeadingWithFilter:(CLLocationDegrees)filter
{
    self.locationManager.headingFilter = filter;
    [self.locationManager startUpdatingHeading];
    self.headingData.headingStatus = HEADINGSTARTING;
}

- (BOOL)locationManagerShouldDisplayHeadingCalibration:(CLLocationManager*)manager
{
    return YES;
}

- (void)locationManager:(CLLocationManager*)manager
       didUpdateHeading:(CLHeading*)heading
{
    CDVHeadingData* hData = self.headingData;

    // normally we would clear the delegate to stop getting these notifications, but
    // we are sharing a CLLocationManager to get location data as well, so we do a nil check here
    // ideally heading and location should use their own CLLocationManager instances
    if (hData == nil) {
        return;
    }

    // save the data for next call into getHeadingData
    hData.headingInfo = heading;
    BOOL bTimeout = NO;
    if (!hData.headingFilter && hData.headingTimestamp) {
        bTimeout = fabs([hData.headingTimestamp timeIntervalSinceNow]) > hData.timeout;
    }

    if (hData.headingStatus == HEADINGSTARTING) {
        hData.headingStatus = HEADINGRUNNING; // so returnHeading info will work

        // this is the first update
        for (NSString* callbackId in hData.headingCallbacks) {
            [self returnHeadingInfo:callbackId keepCallback:NO];
        }

        [hData.headingCallbacks removeAllObjects];
    }
    if (hData.headingFilter) {
        [self returnHeadingInfo:hData.headingFilter keepCallback:YES];
    } else if (bTimeout) {
        [self stopHeading:nil];
    }
    hData.headingStatus = HEADINGRUNNING;  // to clear any error
    __locationStarted = YES;
}

- (void)locationManager:(CLLocationManager*)manager didFailWithError:(NSError*)error
{
    NSLog(@"locationManager::didFailWithError %@", [error localizedFailureReason]);

    // Compass Error
    if ([error code] == kCLErrorHeadingFailure) {
        CDVHeadingData* hData = self.headingData;
        if (hData) {
            if (hData.headingStatus == HEADINGSTARTING) {
                // heading error during startup - report error
                for (NSString* callbackId in hData.headingCallbacks) {
                    CDVPluginResult* result = [CDVPluginResult resultWithStatus:CDVCommandStatus_ERROR messageAsInt:0];
                    [self.commandDelegate sendPluginResult:result callbackId:callbackId];
                }

                [hData.headingCallbacks removeAllObjects];
            } // else for frequency watches next call to getCurrentHeading will report error
            if (hData.headingFilter) {
                CDVPluginResult* resultFilter = [CDVPluginResult resultWithStatus:CDVCommandStatus_ERROR messageAsInt:0];
                [self.commandDelegate sendPluginResult:resultFilter callbackId:hData.headingFilter];
            }
            hData.headingStatus = HEADINGERROR;
        }
    }

    [self.locationManager stopUpdatingLocation];
    __locationStarted = NO;
}

- (void)dealloc
{
    self.locationManager.delegate = nil;
}

- (void)onReset
{
    [self.locationManager stopUpdatingHeading];
    self.headingData = nil;
}

@end
