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
#import <Quartz/Quartz.h>
#import <AppKit/AppKit.h>
#import <Cordova/CDVPlugin.h>



enum CDVDestinationType {
    DestinationTypeDataUrl = 0,
    DestinationTypeFileUri
};
typedef NSUInteger CDVDestinationType;

enum CDVSourceType {
    SourceTypePhotoLibrary = 0,
    SourceTypeCamera,
    SourceTypePhotoAlbum
};
typedef NSUInteger CDVSourceType;

enum CDVEncodingType {
    EncodingTypeJPEG = 0,
    EncodingTypePNG
};
typedef NSUInteger CDVEncodingType;

enum CDVMediaType {
    MediaTypePicture = 0,
    MediaTypeVideo,
    MediaTypeAll
};
typedef NSUInteger CDVMediaType;


// ======================================================================= //


@interface CDVPictureOptions : NSObject

@property (strong) NSNumber *quality;
@property (assign) CDVDestinationType destinationType;
@property (assign) CDVSourceType sourceType;
@property (assign) CGSize targetSize;
@property (assign) CDVEncodingType encodingType;
@property (assign) CDVMediaType mediaType;
@property (assign) BOOL allowsEditing;
@property (assign) BOOL correctOrientation;
@property (assign) BOOL saveToPhotoAlbum;

+ (instancetype) createFromTakePictureArguments:(CDVInvokedUrlCommand *)command;

@end


// ======================================================================= //


@interface CDVCamera : CDVPlugin

- (void)takePicture:(CDVInvokedUrlCommand *)command;
- (void)cleanup:(CDVInvokedUrlCommand *)command;

@end
