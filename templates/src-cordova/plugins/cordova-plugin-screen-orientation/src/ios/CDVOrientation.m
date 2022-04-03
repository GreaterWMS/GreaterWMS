/*
 *
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 *
 */

#import "CDVOrientation.h"
#import <Cordova/CDVViewController.h>
#import <objc/message.h>

@interface CDVOrientation () {}
@end

@implementation CDVOrientation

-(void)screenOrientation:(CDVInvokedUrlCommand *)command
{
    CDVPluginResult* pluginResult;
    NSInteger orientationMask = [[command argumentAtIndex:0] integerValue];
    CDVViewController* vc = (CDVViewController*)self.viewController;
    NSMutableArray* result = [[NSMutableArray alloc] init];
    
    if(orientationMask & 1) {
        [result addObject:[NSNumber numberWithInt:UIInterfaceOrientationPortrait]];
    }
    if(orientationMask & 2) {
        [result addObject:[NSNumber numberWithInt:UIInterfaceOrientationPortraitUpsideDown]];
    }
    if(orientationMask & 4) {
        [result addObject:[NSNumber numberWithInt:UIInterfaceOrientationLandscapeRight]];
    }
    if(orientationMask & 8) {
        [result addObject:[NSNumber numberWithInt:UIInterfaceOrientationLandscapeLeft]];
    }
    
    SEL selector = NSSelectorFromString(@"setSupportedOrientations:");
    
    if([vc respondsToSelector:selector]) {
        if (orientationMask != 15 || [UIDevice currentDevice] == nil) {
            ((void (*)(CDVViewController*, SEL, NSMutableArray*))objc_msgSend)(vc,selector,result);
        }
        
        if ([UIDevice currentDevice] != nil){
            NSNumber *value = nil;
            if (orientationMask != 15) {
                if (!_isLocked) {
                    _lastOrientation = [UIApplication sharedApplication].statusBarOrientation;
                }
                UIInterfaceOrientation deviceOrientation = [UIApplication sharedApplication].statusBarOrientation;
                if(orientationMask == 8  || (orientationMask == 12  && !UIInterfaceOrientationIsLandscape(deviceOrientation))) {
                    value = [NSNumber numberWithInt:UIInterfaceOrientationLandscapeLeft];
                } else if (orientationMask == 4){
                    value = [NSNumber numberWithInt:UIInterfaceOrientationLandscapeRight];
                } else if (orientationMask == 1 || (orientationMask == 3 && !UIInterfaceOrientationIsPortrait(deviceOrientation))) {
                    value = [NSNumber numberWithInt:UIInterfaceOrientationPortrait];
                } else if (orientationMask == 2) {
                    value = [NSNumber numberWithInt:UIInterfaceOrientationPortraitUpsideDown];
                }
            } else {
                if (_lastOrientation != UIInterfaceOrientationUnknown) {
                    [[UIDevice currentDevice] setValue:[NSNumber numberWithInt:_lastOrientation] forKey:@"orientation"];
                    ((void (*)(CDVViewController*, SEL, NSMutableArray*))objc_msgSend)(vc,selector,result);
                    [UINavigationController attemptRotationToDeviceOrientation];
                }
            }
            if (value != nil) {
                _isLocked = true;
                [[UIDevice currentDevice] setValue:value forKey:@"orientation"];
            } else {
                _isLocked = false;
            }
        }
        
        pluginResult = [CDVPluginResult resultWithStatus:CDVCommandStatus_OK];
    }
    else {
        pluginResult = [CDVPluginResult resultWithStatus:CDVCommandStatus_INVALID_ACTION messageAsString:@"Error calling to set supported orientations"];
    }
    
    [self.commandDelegate sendPluginResult:pluginResult callbackId:command.callbackId];
    
}

@end
