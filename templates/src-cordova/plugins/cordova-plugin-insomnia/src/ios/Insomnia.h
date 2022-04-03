#import <Cordova/CDV.h>

@interface Insomnia :CDVPlugin

- (void) keepAwake:(CDVInvokedUrlCommand*)command;

- (void) allowSleepAgain:(CDVInvokedUrlCommand*)command;

@end
