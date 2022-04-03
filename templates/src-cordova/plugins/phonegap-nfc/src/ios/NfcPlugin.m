//
//  NfcPlugin.m
//  PhoneGap NFC - Cordova Plugin
//
//  (c) 2107-2020 Don Coleman

#import "NfcPlugin.h"

@interface NfcPlugin() {
    NSString* sessionCallbackId;
    NSString* channelCallbackId;
    id<NFCNDEFTag> connectedTag API_AVAILABLE(ios(13.0));
    NFCNDEFStatus connectedTagStatus API_AVAILABLE(ios(13.0));
}
@property (nonatomic, assign) BOOL writeMode;
@property (nonatomic, assign) BOOL shouldUseTagReaderSession;
@property (nonatomic, assign) BOOL sendCallbackOnSessionStart;
@property (nonatomic, assign) BOOL returnTagInCallback;
@property (nonatomic, assign) BOOL returnTagInEvent;
@property (nonatomic, assign) BOOL keepSessionOpen;
@property (strong, nonatomic) NFCReaderSession *nfcSession API_AVAILABLE(ios(11.0));
@property (strong, nonatomic) NFCNDEFMessage *messageToWrite API_AVAILABLE(ios(11.0));
@end

@implementation NfcPlugin

- (void)pluginInitialize {

    NSLog(@"PhoneGap NFC - Cordova Plugin");
    NSLog(@"(c) 2017-2020 Don Coleman");

    [super pluginInitialize];
    
    if (@available(iOS 11, *)) {
        if (![NFCNDEFReaderSession readingAvailable]) {
            NSLog(@"NFC Support is NOT available");
        }
    } else {
        NSLog(@"NFC Support is NOT available before iOS 11");
    }
}

#pragma mark - Cordova Plugin Methods

- (void)channel:(CDVInvokedUrlCommand *)command {
    // the channel is used to send NFC tag data to the web view
    channelCallbackId = [command.callbackId copy];
}

- (void)beginSession:(CDVInvokedUrlCommand*)command {
    NSLog(@"beginSession");
    NSLog(@"WARNING: beginSession is deprecated. Use scanNdef or scanTag.");

    self.shouldUseTagReaderSession = NO;
    self.sendCallbackOnSessionStart = YES;  // Not sure why we were doing this
    self.returnTagInCallback = NO;
    self.returnTagInEvent = YES;
    self.keepSessionOpen = NO;

    [self startScanSession:command];
}

- (void)scanNdef:(CDVInvokedUrlCommand*)command {
    NSLog(@"scanNdef");

    self.shouldUseTagReaderSession = NO;
    self.sendCallbackOnSessionStart = NO;
    self.returnTagInCallback = YES;
    self.returnTagInEvent = NO;

    NSArray<NSDictionary *> *options = [command argumentAtIndex:0];
    self.keepSessionOpen = [options valueForKey:@"keepSessionOpen"];

    [self startScanSession:command];
}

- (void)scanTag:(CDVInvokedUrlCommand*)command {
    NSLog(@"scanTag");

    self.shouldUseTagReaderSession = YES;
    self.sendCallbackOnSessionStart = NO;
    self.returnTagInCallback = YES;
    self.returnTagInEvent = NO;

    NSArray<NSDictionary *> *options = [command argumentAtIndex:0];
    self.keepSessionOpen = [options valueForKey:@"keepSessionOpen"];

    [self startScanSession:command];
}

- (void)writeTag:(CDVInvokedUrlCommand*)command API_AVAILABLE(ios(13.0)){
    NSLog(@"writeTag");
    
    self.writeMode = YES;
    self.shouldUseTagReaderSession = NO;
    BOOL reusingSession = NO;
    
    NSArray<NSDictionary *> *ndefData = [command argumentAtIndex:0];

    // Create the NDEF Message
    NSMutableArray<NFCNDEFPayload*> *payloads = [NSMutableArray new];
                              
    @try {
        for (id recordData in ndefData) {
            NSNumber *tnfNumber = [recordData objectForKey:@"tnf"];
            NFCTypeNameFormat tnf = (uint8_t)[tnfNumber intValue];
            NSData *type = [self uint8ArrayToNSData:[recordData objectForKey:@"type"]];
            NSData *identifier = [self uint8ArrayToNSData:[recordData objectForKey:@"identifiers"]];
            NSData *payload  = [self uint8ArrayToNSData:[recordData objectForKey:@"payload"]];
            NFCNDEFPayload *record = [[NFCNDEFPayload alloc] initWithFormat:tnf type:type identifier:identifier payload:payload];
            [payloads addObject:record];
        }
        NSLog(@"%@", payloads);
        NFCNDEFMessage *message = [[NFCNDEFMessage alloc] initWithNDEFRecords:payloads];
        self.messageToWrite = message;
    } @catch(NSException *e) {
        CDVPluginResult *pluginResult = [CDVPluginResult resultWithStatus:CDVCommandStatus_ERROR messageAsString:@"Invalid NDEF Message"];
        [self.commandDelegate sendPluginResult:pluginResult callbackId:command.callbackId];
        return;
    }

    if (self.nfcSession && self.nfcSession.isReady) {       // reuse existing session
        reusingSession = YES;
    } else {                                                // create a new session
        if (self.shouldUseTagReaderSession) {
            NSLog(@"Using NFCTagReaderSession");

            self.nfcSession = [[NFCTagReaderSession new]
                       initWithPollingOption:(NFCPollingISO14443 | NFCPollingISO15693)
                       delegate:self queue:dispatch_get_main_queue()];

        } else {
            NSLog(@"Using NFCTagReaderSession");
            self.nfcSession = [[NFCNDEFReaderSession new]initWithDelegate:self queue:nil invalidateAfterFirstRead:FALSE];
        }
    }

    self.nfcSession.alertMessage = @"Hold near writable NFC tag to update.";
    sessionCallbackId = [command.callbackId copy];

    if (reusingSession) {                   // reusing a read session to write
        self.keepSessionOpen = NO;          // close session after writing
        [self writeNDEFTag:self.nfcSession status:connectedTagStatus tag:connectedTag];
    } else {
        [self.nfcSession beginSession];
    }
}

- (void)cancelScan:(CDVInvokedUrlCommand*)command API_AVAILABLE(ios(11.0)){
    NSLog(@"cancelScan");
    if (self.nfcSession) {
        [self.nfcSession invalidateSession];
    }
    connectedTag = NULL;
    connectedTagStatus = NFCNDEFStatusNotSupported;
    CDVPluginResult *pluginResult = [CDVPluginResult resultWithStatus:CDVCommandStatus_OK];
    [self.commandDelegate sendPluginResult:pluginResult callbackId:command.callbackId];
}

- (void)invalidateSession:(CDVInvokedUrlCommand*)command {
    NSLog(@"invalidateSession");
    NSLog(@"WARNING: invalidateSession is deprecated. Use cancelScan.");
    
    if (_nfcSession) {
        [_nfcSession invalidateSession];
    }
    // Always return OK. Alternately could send status from the NFCNDEFReaderSessionDelegate
    CDVPluginResult *pluginResult = [CDVPluginResult resultWithStatus:CDVCommandStatus_OK];
    [self.commandDelegate sendPluginResult:pluginResult callbackId:command.callbackId];
}

// Nothing happens here, the event listener is registered in JavaScript
- (void)registerNdef:(CDVInvokedUrlCommand *)command {
    NSLog(@"registerNdef");
    CDVPluginResult *pluginResult = [CDVPluginResult resultWithStatus:CDVCommandStatus_OK];
    [self.commandDelegate sendPluginResult:pluginResult callbackId:command.callbackId];
}

// Nothing happens here, the event listener is removed in JavaScript
- (void)removeNdef:(CDVInvokedUrlCommand *)command {
    NSLog(@"removeNdef");
    CDVPluginResult *pluginResult = [CDVPluginResult resultWithStatus:CDVCommandStatus_OK];
    [self.commandDelegate sendPluginResult:pluginResult callbackId:command.callbackId];
}

- (void)enabled:(CDVInvokedUrlCommand *)command {
    NSLog(@"enabled");
    CDVPluginResult *pluginResult;
    if (@available(iOS 11.0, *)) {
        if ([NFCNDEFReaderSession readingAvailable]) {
            pluginResult = [CDVPluginResult resultWithStatus:CDVCommandStatus_OK];
        } else {
            pluginResult = [CDVPluginResult resultWithStatus:CDVCommandStatus_ERROR messageAsString:@"NO_NFC"];
        }
    } else {
        pluginResult = [CDVPluginResult resultWithStatus:CDVCommandStatus_ERROR messageAsString:@"NO_NFC"];
    }
    [self.commandDelegate sendPluginResult:pluginResult callbackId:command.callbackId];
}

#pragma mark - NFCNDEFReaderSessionDelegate

// iOS 11 & 12
- (void) readerSession:(NFCNDEFReaderSession *)session didDetectNDEFs:(NSArray<NFCNDEFMessage *> *)messages API_AVAILABLE(ios(11.0)) {
    NSLog(@"NFCNDEFReaderSession didDetectNDEFs");
    
    session.alertMessage = @"Tag successfully read.";
    for (NFCNDEFMessage *message in messages) {
        [self fireNdefEvent: message];
    }
}

// iOS 13
- (void) readerSession:(NFCNDEFReaderSession *)session didDetectTags:(NSArray<__kindof id<NFCNDEFTag>> *)tags API_AVAILABLE(ios(13.0)) {
    
    if (tags.count > 1) {
        session.alertMessage = @"More than 1 tag detected. Please remove all tags and try again.";
        dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 500 * NSEC_PER_MSEC), dispatch_get_main_queue(), ^{
            NSLog(@"restaring polling");
            [session restartPolling];
        });
        return;
    }
    
    id<NFCNDEFTag> tag = [tags firstObject];
    
    [session connectToTag:tag completionHandler:^(NSError * _Nullable error) {
        if (error) {
            NSLog(@"%@", error);
            [self closeSession:session withError:@"Error connecting to tag."];
            return;
        }
        
        [self processNDEFTag:session tag:tag];
    }];
    
}

- (void) readerSession:(NFCNDEFReaderSession *)session didInvalidateWithError:(NSError *)error API_AVAILABLE(ios(11.0)) {
    NSLog(@"readerSession ended");
    if (error.code == NFCReaderSessionInvalidationErrorFirstNDEFTagRead) { // not an error
        NSLog(@"Session ended after successful NDEF tag read");
        return;
    } else {
        [self sendError:error.localizedDescription];
    }
}

- (void) readerSessionDidBecomeActive:(nonnull NFCReaderSession *)session API_AVAILABLE(ios(11.0)) {
    NSLog(@"readerSessionDidBecomeActive");
    [self sessionDidBecomeActive:session];
}

#pragma mark - NFCTagReaderSessionDelegate

- (void)tagReaderSessionDidBecomeActive:(NFCTagReaderSession *)session API_AVAILABLE(ios(13.0)) {
    NSLog(@"tagReaderSessionDidBecomeActive");
    [self sessionDidBecomeActive:session];
}

- (void)tagReaderSession:(NFCTagReaderSession *)session didDetectTags:(NSArray<__kindof id<NFCTag>> *)tags API_AVAILABLE(ios(13.0)) {
    NSLog(@"tagReaderSession didDetectTags");
    
    if (tags.count > 1) {
        session.alertMessage = @"More than 1 tag detected. Please remove all tags and try again.";
        dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 500 * NSEC_PER_MSEC), dispatch_get_main_queue(), ^{
            NSLog(@"restaring polling");
            [session restartPolling];
        });
        return;
    }
    
    id<NFCTag> tag = [tags firstObject];
    NSMutableDictionary *tagMetaData = [self getTagInfo:tag];
    id<NFCNDEFTag> ndefTag = (id<NFCNDEFTag>)tag;
    
    [session connectToTag:tag completionHandler:^(NSError * _Nullable error) {
        if (error) {
            NSLog(@"%@", error);
            [self closeSession:session withError:@"Error connecting to tag."];
            return;
        }

        [self processNDEFTag:session tag:ndefTag metaData:tagMetaData];
    }];
}

- (void)tagReaderSession:(NFCTagReaderSession *)session didInvalidateWithError:(NSError *)error API_AVAILABLE(ios(13.0)) {
    NSLog(@"tagReaderSession ended");
    [self sendError:error.localizedDescription];
}

#pragma mark - Common NDEF Processing

// Handles scanNdef, scanTag, and beginSession
- (void)startScanSession:(CDVInvokedUrlCommand*)command {
    
    self.writeMode = NO;
    
    NSLog(@"shouldUseTagReaderSession %d", self.shouldUseTagReaderSession);
    NSLog(@"callbackOnSessionStart %d", self.sendCallbackOnSessionStart);
    NSLog(@"returnTagInCallback %d", self.returnTagInCallback);
    NSLog(@"returnTagInEvent %d", self.returnTagInEvent);
    
    if (@available(iOS 13.0, *)) {
        
        if (self.shouldUseTagReaderSession) {
            NSLog(@"Using NFCTagReaderSession");
            self.nfcSession = [[NFCTagReaderSession new]
                           initWithPollingOption:(NFCPollingISO14443 | NFCPollingISO15693)
                           delegate:self queue:dispatch_get_main_queue()];
        } else {
            NSLog(@"Using NFCNDEFReaderSession");
            self.nfcSession = [[NFCNDEFReaderSession new]initWithDelegate:self queue:nil invalidateAfterFirstRead:TRUE];
        }
        sessionCallbackId = [command.callbackId copy];
        self.nfcSession.alertMessage = @"Hold near NFC tag to scan.";
        [self.nfcSession beginSession];
        
    } else if (@available(iOS 11.0, *)) {
        NSLog(@"iOS < 13, using NFCNDEFReaderSession");
        self.nfcSession = [[NFCNDEFReaderSession new]initWithDelegate:self queue:nil invalidateAfterFirstRead:TRUE];
        sessionCallbackId = [command.callbackId copy];
        self.nfcSession.alertMessage = @"Hold near NFC tag to scan.";
        [self.nfcSession beginSession];
    } else {
        NSLog(@"iOS < 11, no NFC support");
        CDVPluginResult *pluginResult;
        pluginResult = [CDVPluginResult resultWithStatus:CDVCommandStatus_ERROR messageAsString:@"NFC requires iOS 11"];
        [self.commandDelegate sendPluginResult:pluginResult callbackId:command.callbackId];
    }
        
}

- (void)processNDEFTag: (NFCReaderSession *)session tag:(__kindof id<NFCNDEFTag>)tag API_AVAILABLE(ios(13.0)) {
    [self processNDEFTag:session tag:tag metaData:[NSMutableDictionary new]];
}

- (void)processNDEFTag: (NFCReaderSession *)session tag:(__kindof id<NFCNDEFTag>)tag metaData: (NSMutableDictionary * _Nonnull)metaData API_AVAILABLE(ios(13.0)) {
                            
    [tag queryNDEFStatusWithCompletionHandler:^(NFCNDEFStatus status, NSUInteger capacity, NSError * _Nullable error) {
        if (error) {
            NSLog(@"%@", error);
            [self closeSession:session withError:@"Error getting tag status."];
            return;
        }
                
        if (self.writeMode) {
            [self writeNDEFTag:session status:status tag:tag];
        } else {
            // save tag & status so we can re-use in write
            if (self.keepSessionOpen) {
                self->connectedTagStatus = status;
                self->connectedTag = tag;
            }
            [self readNDEFTag:session status:status tag:tag metaData:metaData];
        }

    }];
}

- (void)readNDEFTag:(NFCReaderSession * _Nonnull)session status:(NFCNDEFStatus)status tag:(id<NFCNDEFTag>)tag metaData:(NSMutableDictionary * _Nonnull)metaData  API_AVAILABLE(ios(13.0)){
        
    if (status == NFCNDEFStatusNotSupported) {
        NSLog(@"Tag does not support NDEF");
        [self fireTagEvent:metaData];
        [self closeSession:session];
        return;
    }
    
    if (status == NFCNDEFStatusReadOnly) {
        metaData[@"isWritable"] = @FALSE;
    } else if (status == NFCNDEFStatusReadWrite) {
        metaData[@"isWritable"] = @TRUE;
    }
    
    [tag readNDEFWithCompletionHandler:^(NFCNDEFMessage * _Nullable message, NSError * _Nullable error) {

        // Error Code=403 "NDEF tag does not contain any NDEF message" is not an error for this plugin
        if (error && error.code != 403) {
            NSLog(@"%@", error);
            [self closeSession:session withError:@"Read Failed."];
            return;
        } else {
            NSLog(@"%@", message);
            session.alertMessage = @"Tag successfully read.";
            [self fireNdefEvent:message metaData:metaData];
            [self closeSession:session];
        }

    }];

}

- (void)writeNDEFTag:(NFCReaderSession * _Nonnull)session status:(NFCNDEFStatus)status tag:(id<NFCNDEFTag>)tag  API_AVAILABLE(ios(13.0)){
    switch (status) {
        case NFCNDEFStatusNotSupported:
            [self closeSession:session withError:@"Tag is not NDEF compliant."];  // alternate message "Tag does not support NDEF."
            break;
        case NFCNDEFStatusReadOnly:
            [self closeSession:session withError:@"Tag is read only."];
            break;
        case NFCNDEFStatusReadWrite: {
            
            [tag writeNDEF: self.messageToWrite completionHandler:^(NSError * _Nullable error) {
                if (error) {
                    NSLog(@"%@", error);
                    [self closeSession:session withError:@"Write failed."];
                } else {
                    session.alertMessage = @"Wrote data to NFC tag.";
                    CDVPluginResult *pluginResult = [CDVPluginResult resultWithStatus:CDVCommandStatus_OK];
                    [self.commandDelegate sendPluginResult:pluginResult callbackId:self->sessionCallbackId];
                    [self closeSession:session];
                }
            }];
            break;
            
        }
        default:
            [self closeSession:session withError:@"Unknown NDEF tag status."];
    }
}

#pragma mark - Tag Reader Helper Functions

// Gets the tag meta data - type and uid
- (NSMutableDictionary *) getTagInfo:(id<NFCTag>)tag API_AVAILABLE(ios(13.0)) {
    
    NSMutableDictionary *tagInfo = [NSMutableDictionary new];
    
    NSData *uid;
    NSString *type;
    
    switch (tag.type) {
        case NFCTagTypeFeliCa:
            type = @"NFCTagTypeFeliCa";
            uid = nil;
            break;
        case NFCTagTypeMiFare:
            type = @"NFCTagTypeMiFare";
            uid = [[tag asNFCMiFareTag] identifier];
            break;
        case NFCTagTypeISO15693:
            type = @"NFCTagTypeISO15693";
            uid = [[tag asNFCISO15693Tag] identifier];
            break;
        case NFCTagTypeISO7816Compatible:
            type = @"NFCTagTypeISO7816Compatible";
            uid = [[tag asNFCISO7816Tag] identifier];
            break;
        default:
            type = @"Unknown";
            uid = nil;
            break;
    }
                    
    NSLog(@"getTagInfo: %@ with uid %@", type, uid);
    
    [tagInfo setValue:type forKey:@"type"];
    if (uid) {
        [tagInfo setValue:uid forKey:@"id"];
    }
    return tagInfo;
}

#pragma mark - internal implementation

- (void) sendError:(NSString *)message {
    // only send the error if the callback id exists
    if (sessionCallbackId) {
        NSLog(@"sendError: %@", message);
        CDVPluginResult *pluginResult = [CDVPluginResult resultWithStatus:CDVCommandStatus_ERROR messageAsString:message];
        [self.commandDelegate sendPluginResult:pluginResult callbackId:sessionCallbackId];
    }
}

- (void) sessionDidBecomeActive:(NFCReaderSession *) session  API_AVAILABLE(ios(11.0)){
    if (sessionCallbackId && self.sendCallbackOnSessionStart) {
        CDVPluginResult *pluginResult = [CDVPluginResult resultWithStatus:CDVCommandStatus_OK];
        [pluginResult setKeepCallback:@YES];
        [self.commandDelegate sendPluginResult:pluginResult callbackId:sessionCallbackId];
    }
}

- (void) closeSession:(NFCReaderSession *) session  API_AVAILABLE(ios(11.0)){

    // this is a hack to keep a read session open to allow writing
    if (self.keepSessionOpen) {
        return;
    }

    // kill the callback so the Cordova doesn't get "Session invalidated by user"
    sessionCallbackId = NULL;
    connectedTag = NULL;
    connectedTagStatus = NFCNDEFStatusNotSupported;
    [session invalidateSession];
}

- (void) closeSession:(NFCReaderSession *) session withError:(NSString *) errorMessage  API_AVAILABLE(ios(11.0)){
    [self sendError:errorMessage];

    // kill the callback so Cordova doesn't get "Session invalidated by user"
    sessionCallbackId = NULL;
    connectedTag = NULL;
    connectedTagStatus = NFCNDEFStatusNotSupported;
    
    if (@available(iOS 13.0, *)) {
        [session invalidateSessionWithErrorMessage:errorMessage];
    } else {
        [session invalidateSession];
    }
}

-(void) fireTagEvent:(NSDictionary *)metaData API_AVAILABLE(ios(11.0)) {
    // Data is from a tag, but still ends up as an NDEF event in Javascript
    [self fireNdefEvent:nil metaData:metaData];
}

-(void) fireNdefEvent:(NFCNDEFMessage *) ndefMessage API_AVAILABLE(ios(11.0)) {
    [self fireNdefEvent:ndefMessage metaData:nil];
}

// TODO rename method since we're using the channel or callback instead of firing an event
-(void) fireNdefEvent:(NFCNDEFMessage *) ndefMessage metaData:(NSDictionary *)metaData API_AVAILABLE(ios(11.0)) {
    NSLog(@"fireNdefEvent");
    
    NSMutableDictionary *nfcEvent = [NSMutableDictionary new];
    nfcEvent[@"type"] = @"ndef";
    nfcEvent[@"tag"] = [self buildTagDictionary:ndefMessage metaData:metaData];

    if (sessionCallbackId && self.returnTagInCallback) {
        NSLog(@"Sending NFC data via sessionCallbackId");
        CDVPluginResult *pluginResult = [CDVPluginResult resultWithStatus:CDVCommandStatus_OK messageAsDictionary:nfcEvent[@"tag"]];
//        [pluginResult setKeepCallback:[NSNumber numberWithBool:YES]];
        [self.commandDelegate sendPluginResult:pluginResult callbackId:sessionCallbackId];
        sessionCallbackId = NULL;
    }
    
    if (channelCallbackId && self.returnTagInEvent) {
        NSLog(@"Sending NFC data via channelCallbackId so an NDEF event fires)");
        
        CDVPluginResult *pluginResult = [CDVPluginResult resultWithStatus:CDVCommandStatus_OK messageAsDictionary:nfcEvent];
        [pluginResult setKeepCallback:[NSNumber numberWithBool:YES]];
        [self.commandDelegate sendPluginResult:pluginResult callbackId:channelCallbackId];
    }
}

// NSDictionary representing an NFC tag
// NSData fields are converted to uint8_t arrays
-(NSDictionary *) buildTagDictionary:(NFCNDEFMessage *) ndefMessage metaData: (NSDictionary *)metaData API_AVAILABLE(ios(11.0)) {
    
    NSMutableDictionary *dictionary = [NSMutableDictionary new];
    
    // start with tag meta data
    if (metaData) {
        [dictionary setDictionary:metaData];
    }

    // convert uid from NSData to a uint8_t array
    NSData *uid = [dictionary objectForKey:@"id"];
    if (uid) {
        dictionary[@"id"] = [self uint8ArrayFromNSData: uid];
    }
    
    if (ndefMessage) {
        NSMutableArray *array = [NSMutableArray new];
        for (NFCNDEFPayload *record in ndefMessage.records){
            NSDictionary* recordDictionary = [self ndefRecordToNSDictionary:record];
            [array addObject:recordDictionary];
        }
        [dictionary setObject:array forKey:@"ndefMessage"];
    }
    
    return [dictionary copy];
}

-(NSDictionary *) ndefRecordToNSDictionary:(NFCNDEFPayload *) ndefRecord API_AVAILABLE(ios(11.0)) {
    NSMutableDictionary *dict = [NSMutableDictionary new];
    dict[@"tnf"] = [NSNumber numberWithInt:(int)ndefRecord.typeNameFormat];
    dict[@"type"] = [self uint8ArrayFromNSData: ndefRecord.type];
    dict[@"id"] = [self uint8ArrayFromNSData: ndefRecord.identifier];
    dict[@"payload"] = [self uint8ArrayFromNSData: ndefRecord.payload];
    NSDictionary *copy = [dict copy];
    return copy;
}

- (NSArray *) uint8ArrayFromNSData:(NSData *) data {
    const void *bytes = [data bytes];
    NSMutableArray *array = [NSMutableArray array];
    for (NSUInteger i = 0; i < [data length]; i += sizeof(uint8_t)) {
        uint8_t elem = OSReadLittleInt(bytes, i);
        [array addObject:[NSNumber numberWithInt:elem]];
    }
    return array;
}

- (NSData *) uint8ArrayToNSData:(NSArray *) array {
    // NSLog(@"nsDataFromUint8Array input %@", array);
    
    NSMutableData *data = [[NSMutableData alloc] initWithCapacity: [array count]];
    for (NSNumber *number in array) {
        uint8_t b = (uint8_t)[number unsignedIntValue];
        // NSLog(@"> %hhu", b);
        [data appendBytes:&b length:1];
    }
    return data;
}

- (NSString*) dictionaryAsJSONString:(NSDictionary *)dict {
    NSError *error;
    NSData *jsonData = [NSJSONSerialization dataWithJSONObject:dict options:0 error:&error];
    NSString *jsonString;
    if (! jsonData) {
        jsonString = [NSString stringWithFormat:@"Error creating JSON for NDEF Message: %@", error];
        NSLog(@"%@", jsonString);
    } else {
        jsonString = [[NSString alloc] initWithData:jsonData encoding:NSUTF8StringEncoding];
    }
    return jsonString;
}

@end
