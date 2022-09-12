/*
 * Copyright (c) Microsoft Open Technologies, Inc. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
 */

namespace WinRTBarcodeReader
{
    using System;
    using System.Threading;
    using System.Threading.Tasks;

    using Windows.Foundation;
    using Windows.Graphics.Imaging;
    using Windows.Media.Capture;
    using Windows.Media.MediaProperties;
    using Windows.Storage.Streams;

    using ZXing;

    /// <summary>
    /// Defines the Reader type, that perform barcode search asynchronously.
    /// </summary>
    public sealed class Reader
    {
        #region Private fields

        /// <summary>
        ///     Data reader, used to create bitmap array.
        /// </summary>
        private BarcodeReader barcodeReader;

        /// <summary>
        ///     The cancel search flag.
        /// </summary>
        private CancellationTokenSource cancelSearch;

        /// <summary>
        ///     MediaCapture instance, used for barcode search.
        /// </summary>
        private MediaCapture capture;

        /// <summary>
        ///     Encoding properties for mediaCapture object.
        /// </summary>
        private ImageEncodingProperties encodingProps;

        /// <summary>
        ///     Flag that indicates successful barcode search.
        /// </summary>
        private bool barcodeFoundOrCancelled;

        /// <summary>
        ///     Image stream for MediaCapture content.
        /// </summary>
        private InMemoryRandomAccessStream imageStream;

        #endregion

        #region Constructor

        /// <summary>
        /// Initializes a new instance of the <see cref="Reader" /> class.
        /// </summary>
        /// <param name="capture">MediaCapture instance.</param>
        /// <param name="width">Capture frame width.</param>
        /// <param name="height">Capture frame height.</param>
        public void Init(MediaCapture capture, uint width, uint height)
        {
            this.capture = capture;
            encodingProps = ImageEncodingProperties.CreateJpeg();
            encodingProps.Width = width;
            encodingProps.Height = height;

            barcodeReader = new BarcodeReader {Options = {TryHarder = true}};
            cancelSearch = new CancellationTokenSource();
        }

        #endregion

        #region Public methods

        /// <summary>
        /// Perform async MediaCapture analysis and searches for barcode.
        /// </summary>
        /// <returns>IAsyncOperation object</returns>
        public IAsyncOperation<Result> ReadCode()
        {
            return this.Read().AsAsyncOperation();
        }

        /// <summary>
        /// Send signal to stop barcode search.
        /// </summary>
        public void Stop()
        {
            this.cancelSearch.Cancel();
        }

        #endregion

        #region Private methods

        /// <summary>
        /// Perform async MediaCapture analysis and searches for barcode.
        /// </summary>
        /// <returns>Task object</returns>
        private async Task<Result> Read()
        {
            Result result = null;
            try
            {
                while (result == null)
                {
                    result = await GetCameraImage(cancelSearch.Token);
                }
            }
            catch (OperationCanceledException) { }

            return result;
        }

        /// <summary>
        /// Perform image capture from mediaCapture object
        /// </summary>
        /// <param name="cancelToken">
        /// The cancel Token.
        /// </param>
        /// <returns>
        /// Decoded barcode string.
        /// </returns>
        private async Task<Result> GetCameraImage(CancellationToken cancelToken)
        {
            if (cancelToken.IsCancellationRequested)
            {
                throw new OperationCanceledException(cancelToken);
            }

            imageStream = new InMemoryRandomAccessStream();

            await capture.CapturePhotoToStreamAsync(encodingProps, imageStream);
            await imageStream.FlushAsync();

            var decoder = await BitmapDecoder.CreateAsync(imageStream);

            byte[] pixels =
                (await
                    decoder.GetPixelDataAsync(BitmapPixelFormat.Rgba8,
                        BitmapAlphaMode.Ignore,
                        new BitmapTransform(),
                        ExifOrientationMode.IgnoreExifOrientation,
                        ColorManagementMode.DoNotColorManage)).DetachPixelData();

            const BitmapFormat format = BitmapFormat.RGB32;

            imageStream.Dispose();

            var result =
                await
                    Task.Run(
                        () => barcodeReader.Decode(pixels, (int) decoder.PixelWidth, (int) decoder.PixelHeight, format),
                        cancelToken);

            return result;
        }

        #endregion
    }
}
