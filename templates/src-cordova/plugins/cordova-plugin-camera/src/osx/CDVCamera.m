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
#import "CDVCamera.h"


@implementation CDVPictureOptions

+ (instancetype) createFromTakePictureArguments:(CDVInvokedUrlCommand*)command {
    CDVPictureOptions *pictureOptions = [[CDVPictureOptions alloc] init];

    pictureOptions.quality = [command argumentAtIndex:0 withDefault:@(50)];
    pictureOptions.destinationType = [[command argumentAtIndex:1 withDefault:@(DestinationTypeFileUri)] unsignedIntegerValue];
    pictureOptions.sourceType = [[command argumentAtIndex:2 withDefault:@(SourceTypeCamera)] unsignedIntegerValue];

    NSNumber *targetWidth = [command argumentAtIndex:3 withDefault:nil];
    NSNumber *targetHeight = [command argumentAtIndex:4 withDefault:nil];
    pictureOptions.targetSize = CGSizeMake(0, 0);
    if ((targetWidth != nil) && (targetHeight != nil)) {
        pictureOptions.targetSize = CGSizeMake([targetWidth floatValue], [targetHeight floatValue]);
    }

    pictureOptions.encodingType = [[command argumentAtIndex:5 withDefault:@(EncodingTypeJPEG)] unsignedIntegerValue];
    pictureOptions.mediaType = [[command argumentAtIndex:6 withDefault:@(MediaTypePicture)] unsignedIntegerValue];
    pictureOptions.allowsEditing = [[command argumentAtIndex:7 withDefault:@(NO)] boolValue];
    pictureOptions.correctOrientation = [[command argumentAtIndex:8 withDefault:@(NO)] boolValue];
    pictureOptions.saveToPhotoAlbum = [[command argumentAtIndex:9 withDefault:@(NO)] boolValue];

    return pictureOptions;
}

@end


// ======================================================================= //


@implementation CDVCamera

/*!
 Static array that stores the temporary created files allowing to delete them when calling navigator.camera.cleanup(...)
 */
static NSMutableArray *cleanUpFiles;

+ (void)initialize {
    cleanUpFiles = [NSMutableArray array];
}

- (void)takePicture:(CDVInvokedUrlCommand *)command {
    CDVPictureOptions *pictureOptions = [CDVPictureOptions createFromTakePictureArguments:command];
    if (pictureOptions.sourceType == SourceTypeCamera) {
        [self takePictureFromCamera:command withOptions:pictureOptions];
    } else {
        [self takePictureFromFile:command withOptions:pictureOptions];
    }
}

- (void)cleanup:(CDVInvokedUrlCommand*)command {
    [self.commandDelegate runInBackground:^{
        if (cleanUpFiles.count > 0) {
            for (int i=0; i<cleanUpFiles.count; i++) {
                NSString *path = [cleanUpFiles objectAtIndex:i];
                [[NSFileManager defaultManager] removeItemAtPath:path error:nil];
            }

            [cleanUpFiles removeAllObjects];

            CDVPluginResult *result = [CDVPluginResult resultWithStatus:CDVCommandStatus_OK];
            [self.commandDelegate sendPluginResult:result callbackId:command.callbackId];
        }
    }];
}


#pragma mark - Camera

/*!
 Takes a picture from the iSight camera using the default OS dialog.
 @see https://developer.apple.com/documentation/quartz/ikpicturetaker
 */
- (void)takePictureFromCamera:(CDVInvokedUrlCommand *)command withOptions:(CDVPictureOptions *)pictureOptions {
    IKPictureTaker *pictureTaker = [IKPictureTaker pictureTaker];
    [pictureTaker setValue:[NSNumber numberWithBool:YES] forKey:IKPictureTakerAllowsVideoCaptureKey];
    [pictureTaker setValue:[NSNumber numberWithBool:NO]  forKey:IKPictureTakerAllowsFileChoosingKey];
    [pictureTaker setValue:[NSNumber numberWithBool:pictureOptions.allowsEditing] forKey:IKPictureTakerShowEffectsKey];
    [pictureTaker setValue:[NSNumber numberWithBool:pictureOptions.allowsEditing] forKey:IKPictureTakerAllowsEditingKey];

    NSDictionary *contextInfo = @{ @"command": command, @"pictureOptions" : pictureOptions};
    [pictureTaker beginPictureTakerSheetForWindow:self.viewController.contentView.window withDelegate:self didEndSelector:@selector(pictureTakerDidEnd:returnCode:contextInfo:) contextInfo:(void *)CFBridgingRetain(contextInfo)];

}

- (void)pictureTakerDidEnd:(IKPictureTaker *)pictureTaker returnCode:(NSInteger)returnCode contextInfo:(void  *)contextInfo {
    if (returnCode == NSOKButton) {
        NSDictionary *contextInfoDictionary = (NSDictionary *)CFBridgingRelease(contextInfo);
        CDVInvokedUrlCommand *command = [contextInfoDictionary valueForKey:@"command"];
        CDVPictureOptions *pictureOptions = [contextInfoDictionary valueForKey:@"pictureOptions"];

        [self returnImage:pictureTaker.outputImage command:command options:pictureOptions];
    }
}


#pragma mark - File

/*!
 Allows to select an image or video using the system native dialog.
 */
- (void)takePictureFromFile:(CDVInvokedUrlCommand *)command withOptions:(CDVPictureOptions *)pictureOptions {
    NSOpenPanel *openPanel = [NSOpenPanel openPanel];
    openPanel.canChooseFiles = YES;
    openPanel.canChooseDirectories = NO;
    openPanel.canCreateDirectories = YES;
    openPanel.allowsMultipleSelection = NO;

    NSMutableArray *allowedTypes = [NSMutableArray array];
    if (pictureOptions.mediaType == MediaTypePicture || pictureOptions.mediaType == MediaTypeAll) {
        [allowedTypes addObjectsFromArray:[NSImage imageTypes]];
    }
    if (pictureOptions.mediaType == MediaTypeVideo || pictureOptions.mediaType == MediaTypeAll) {
        [allowedTypes addObjectsFromArray:@[(NSString *)kUTTypeMovie]];
    }
    [openPanel setAllowedFileTypes:allowedTypes];

    [openPanel beginSheetModalForWindow:self.viewController.contentView.window completionHandler:^(NSInteger result) {
        if (result == NSOKButton) {
            NSURL *fileURL = [openPanel.URLs objectAtIndex:0];

            if ([self fileIsImage:fileURL]) {
                NSImage *image = [[NSImage alloc] initWithContentsOfFile:fileURL.path];
                [self returnImage:image command:command options:pictureOptions];
            } else {
                if (pictureOptions.destinationType == DestinationTypeDataUrl) {
                    CDVPluginResult *result = [CDVPluginResult resultWithStatus:CDVCommandStatus_ERROR messageAsString:@"Camera.DestinationType.DATA_URL is only available with image files"];
                    [self.commandDelegate sendPluginResult:result callbackId:command.callbackId];
                } else {
                    [self returnUri:fileURL.path command:command options:pictureOptions];
                }
            }
        }
    }];
}


#pragma mark - Common

/*!
 Returns to JavaScript a URI.
 Called when Camera.DestinationType.FILE_URI.
 */
- (void)returnUri:(NSString *)path command:(CDVInvokedUrlCommand *)command options:(CDVPictureOptions *)pictureOptions {
    NSString *protocol = (pictureOptions.destinationType == DestinationTypeFileUri) ? @"file://" : @"";
    NSString *uri = [NSString stringWithFormat:@"%@%@", protocol, path];

    CDVPluginResult *result = [CDVPluginResult resultWithStatus:CDVCommandStatus_OK messageAsString:uri];
    [self.commandDelegate sendPluginResult:result callbackId:command.callbackId];
}

/*!
 Returns to JavaScript a base64 encoded image.
 Called when Camera.DestinationType.DATA_URL.
 */
- (void)returnImage:(NSImage *)image command:(CDVInvokedUrlCommand *)command options:(CDVPictureOptions *)pictureOptions {
    [self.commandDelegate runInBackground:^{
        NSData *processedImageData = [self processImage:image options:pictureOptions];

        if (pictureOptions.destinationType == DestinationTypeDataUrl) {
            CDVPluginResult *result = [CDVPluginResult resultWithStatus:CDVCommandStatus_OK messageAsString:[processedImageData base64EncodedStringWithOptions:NSDataBase64EncodingEndLineWithLineFeed]];
            [self.commandDelegate sendPluginResult:result callbackId:command.callbackId];
        } else {
            NSString *tempFilePath = [self uniqueImageName:pictureOptions];
            [processedImageData writeToFile:tempFilePath atomically:YES];
            [cleanUpFiles addObject:tempFilePath];
            [self returnUri:tempFilePath command:command options:pictureOptions];
        }
    }];

}

/*!
 Top level method to apply the size and quality required changes to an image.
 */
- (NSData *)processImage:(NSImage *)image options:(CDVPictureOptions *)pictureOptions {
    NSImage *sourceImage = image;
    if (pictureOptions.targetSize.width > 0 && pictureOptions.targetSize.height > 0) {
        sourceImage = [self resizeImage:sourceImage toSize:pictureOptions.targetSize];
    }

    CGImageRef cgRef = [sourceImage CGImageForProposedRect:NULL context:nil hints:nil];
    NSBitmapImageRep *imageRepresentation = [[NSBitmapImageRep alloc] initWithCGImage:cgRef];

    NSData *data = (pictureOptions.encodingType == EncodingTypeJPEG)
    ? [imageRepresentation representationUsingType:NSJPEGFileType properties:@{NSImageCompressionFactor: [NSNumber numberWithFloat:pictureOptions.quality.floatValue/100.f]}]
    : [imageRepresentation representationUsingType:NSPNGFileType  properties:@{NSImageCompressionFactor: @1.0}];

    return data;
}

/*!
 Auxiliar method to resize an image.
 */
- (NSImage *)resizeImage:(NSImage *)image toSize:(CGSize)newSize {
    CGFloat aspectWidth  = newSize.width  / image.size.width;
    CGFloat aspectHeight = newSize.height / image.size.height;
    CGFloat aspectRatio  = MIN(aspectWidth, aspectHeight);

    CGSize scaledSize = NSMakeSize(image.size.width*aspectRatio, image.size.height*aspectRatio);

    NSImage *smallImage = [[NSImage alloc] initWithSize: scaledSize];
    [smallImage lockFocus];
    [image setSize: scaledSize];
    [[NSGraphicsContext currentContext] setImageInterpolation:NSImageInterpolationHigh];
    [image drawAtPoint:NSZeroPoint fromRect:CGRectMake(0, 0, scaledSize.width, scaledSize.height) operation:NSCompositeCopy fraction:1.0];
    [smallImage unlockFocus];
    return smallImage;
}

/*!
 Auxiliar method to know if a given file is an image or not.
 */
- (BOOL)fileIsImage:(NSURL *)fileURL {
    NSString *type;
    BOOL isImage = NO;

    if ([fileURL getResourceValue:&type forKey:NSURLTypeIdentifierKey error:nil]) {
        isImage = [[NSImage imageTypes] containsObject:type];
    }

    return isImage;
}

/*!
 Auxiliar method that generates an unique filename for an image in the temporary directory.
 */
- (NSString *)uniqueImageName:(CDVPictureOptions *)pictureOptions {
    NSString *tempDir   = NSTemporaryDirectory();
    NSString *guid      = [[NSProcessInfo processInfo] globallyUniqueString] ;
    NSString *extension = (pictureOptions.encodingType == EncodingTypeJPEG) ? @"jpeg" : @"png";
    NSString *uniqueFileName = [NSString stringWithFormat:@"%@%@.%@", tempDir, guid, extension];
    return uniqueFileName;
}

@end