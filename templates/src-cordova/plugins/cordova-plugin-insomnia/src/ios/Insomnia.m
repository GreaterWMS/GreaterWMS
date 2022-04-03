#import "Insomnia.h"
#import <Cordova/CDV.h>

@implementation Insomnia

- (void) keepAwake:(CDVInvokedUrlCommand*)command {
  NSString *callbackId = command.callbackId;

  // Acquire a reference to the local UIApplication singleton
  UIApplication* app = [UIApplication sharedApplication];

  if (![app isIdleTimerDisabled]) {
    [app setIdleTimerDisabled:true];
  }
  CDVPluginResult* result = [CDVPluginResult resultWithStatus:CDVCommandStatus_OK];
  [self.commandDelegate sendPluginResult:result callbackId:callbackId];
}

- (void) allowSleepAgain:(CDVInvokedUrlCommand*)command {
  NSString *callbackId = command.callbackId;

  // Acquire a reference to the local UIApplication singleton
  UIApplication* app = [UIApplication sharedApplication];

  if([app isIdleTimerDisabled]) {
    [app setIdleTimerDisabled:false];
  }
  CDVPluginResult* result = [CDVPluginResult resultWithStatus:CDVCommandStatus_OK];
  [self.commandDelegate sendPluginResult:result callbackId:callbackId];
}

@end