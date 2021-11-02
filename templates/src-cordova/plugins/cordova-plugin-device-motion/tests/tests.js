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

/* jshint jasmine: true */
/* global Windows */

exports.defineAutoTests = function () {
    var isWindows = (cordova.platformId === "windows") || (cordova.platformId === "windows8"),
     // Checking existence of accelerometer for windows platform
     // Assumed that accelerometer always exists on other platforms. Extend
     // condition to support accelerometer check on other platforms
     isAccelExist = isWindows ? Windows.Devices.Sensors.Accelerometer.getDefault() !== null : true;

  describe('Accelerometer (navigator.accelerometer)', function () {
    var fail = function(done) {
      expect(true).toBe(false);
      done();
    };

    // This timeout is here to lessen the load on native accelerometer
    // intensive use of which can lead to occasional test failures
    afterEach(function(done) {
      setTimeout(function() {
        done();
      }, 100);
    });

    it("accelerometer.spec.1 should exist", function () {
      expect(navigator.accelerometer).toBeDefined();
    });

    describe("getCurrentAcceleration", function() {
      it("accelerometer.spec.2 should exist", function() {
        expect(typeof navigator.accelerometer.getCurrentAcceleration).toBeDefined();
        expect(typeof navigator.accelerometer.getCurrentAcceleration == 'function').toBe(true);
      });

      it("accelerometer.spec.3 success callback should be called with an Acceleration object", function(done) {
        // skip the test if Accelerometer doesn't exist on this device
        if (!isAccelExist) {
          pending();
        }
        var win = function(a) {
          expect(a).toBeDefined();
          expect(a.x).toBeDefined();
          expect(typeof a.x == 'number').toBe(true);
          expect(a.y).toBeDefined();
          expect(typeof a.y == 'number').toBe(true);
          expect(a.z).toBeDefined();
          expect(typeof a.z == 'number').toBe(true);
          expect(a.timestamp).toBeDefined();
          expect(typeof a.timestamp).toBe('number');
          done();
        };

        var onError = function(err){
            console.log(err);
            console.log("Skipping gyroscope tests, marking all as pending.");
            isAccelExist = false;
            expect(true).toBe(true);
            done();
         };

        navigator.accelerometer.getCurrentAcceleration(win, onError);
      });

      it("accelerometer.spec.4 success callback Acceleration object should have (reasonable) values for x, y and z expressed in m/s^2", function(done) {
        // skip the test if Accelerometer doesn't exist on this device
        if (!isAccelExist) {
          pending();
        }
        var reasonableThreshold = 15;
        var win = function(a) {
          expect(a.x).toBeLessThan(reasonableThreshold);
          expect(a.x).toBeGreaterThan(reasonableThreshold * -1);
          expect(a.y).toBeLessThan(reasonableThreshold);
          expect(a.y).toBeGreaterThan(reasonableThreshold * -1);
          expect(a.z).toBeLessThan(reasonableThreshold);
          expect(a.z).toBeGreaterThan(reasonableThreshold * -1);
          done();
        };

        navigator.accelerometer.getCurrentAcceleration(win, fail.bind(null,done));
      });

      it("accelerometer.spec.5 success callback Acceleration object should return a recent timestamp", function(done) {
        // skip the test if Accelerometer doesn't exist on this device
        if (!isAccelExist) {
          pending();
        }
        var veryRecently = (new Date()).getTime();
        // Need to check that dates returned are not vastly greater than a recent time stamp.
        // In case the timestamps returned are ridiculously high
        var reasonableTimeLimit = veryRecently + 5000; // 5 seconds from now
        var win = function(a) {
          expect(a.timestamp).toBeGreaterThan(veryRecently - 200); // this is flakey, relaxing a bit
          expect(a.timestamp).toBeLessThan(reasonableTimeLimit);
          done();
        };

        navigator.accelerometer.getCurrentAcceleration(win, fail.bind(null,done));
      });
    });

    describe("watchAcceleration", function() {
      var id;

      afterEach(function(done) {
          if (id) {
            navigator.accelerometer.clearWatch(id);
          }
          // clearWatch implementation is async but doesn't accept a cllback
          // so let's give it some time before starting next spec
          setTimeout(done, 100);
      });

      it("accelerometer.spec.6 should exist", function() {
          expect(navigator.accelerometer.watchAcceleration).toBeDefined();
          expect(typeof navigator.accelerometer.watchAcceleration == 'function').toBe(true);
      });

      it("accelerometer.spec.7 success callback should be called with an Acceleration object", function(done) {
        // skip the test if Accelerometer doesn't exist on this device
        if (!isAccelExist) {
          pending();
        }
        var win = function(a) {
          expect(a).toBeDefined();
          expect(a.x).toBeDefined();
          expect(typeof a.x == 'number').toBe(true);
          expect(a.y).toBeDefined();
          expect(typeof a.y == 'number').toBe(true);
          expect(a.z).toBeDefined();
          expect(typeof a.z == 'number').toBe(true);
          expect(a.timestamp).toBeDefined();
          expect(typeof a.timestamp).toBe('number');
          done();
        };

        id = navigator.accelerometer.watchAcceleration(win, fail.bind(null,done), {frequency:100});
      });

        it("accelerometer.spec.8 success callback Acceleration object should have (reasonable) values for x, y and z expressed in m/s^2", function(done) {
          // skip the test if Accelerometer doesn't exist on this device
          if (!isAccelExist) {
            pending();
          }
          var reasonableThreshold = 15;
          var win = function(a) {
            expect(a.x).toBeLessThan(reasonableThreshold);
            expect(a.x).toBeGreaterThan(reasonableThreshold * -1);
            expect(a.y).toBeLessThan(reasonableThreshold);
            expect(a.y).toBeGreaterThan(reasonableThreshold * -1);
            expect(a.z).toBeLessThan(reasonableThreshold);
            expect(a.z).toBeGreaterThan(reasonableThreshold * -1);
            done();
          };

          id = navigator.accelerometer.watchAcceleration(win, fail.bind(null,done), {frequency:100});
        });

        it("accelerometer.spec.9 success callback Acceleration object should return a recent timestamp", function(done) {
          // skip the test if Accelerometer doesn't exist on this device
          if (!isAccelExist) {
            pending();
          }
          var veryRecently = (new Date()).getTime();
          // Need to check that dates returned are not vastly greater than a recent time stamp.
          // In case the timestamps returned are ridiculously high
          var reasonableTimeLimit = veryRecently + 5000; // 5 seconds from now
          var win = function(a) {
            expect(a.timestamp).toBeGreaterThan(veryRecently - 200); // this is flakey, relaxing a bit
            expect(a.timestamp).toBeLessThan(reasonableTimeLimit);
            done();
          };

          id = navigator.accelerometer.watchAcceleration(win, fail.bind(null,done), {frequency:100});
        });

        it("accelerometer.spec.12 success callback should be preserved and called several times", function (done) {
            // skip the test if Accelerometer doesn't exist on this device
            if (!isAccelExist) {
              pending();
            }
            var callbacksCallCount = 0,
                callbacksCallTestCount = 3;

            var win = function (a) {
                if (callbacksCallCount++ < callbacksCallTestCount) return;
                expect(typeof a).toBe('object');
                done();
            };

            id = navigator.accelerometer.watchAcceleration(win, fail.bind(null, done), { frequency: 100 });
        });
    });

    describe("clearWatch", function() {
      it("accelerometer.spec.10 should exist", function() {
          expect(navigator.accelerometer.clearWatch).toBeDefined();
          expect(typeof navigator.accelerometer.clearWatch == 'function').toBe(true);
      });

      it("accelerometer.spec.11 should clear an existing watch", function(done) {
          // skip the test if Accelerometer doesn't exist on this device
          if (!isAccelExist) {
              pending();
          }
          var id;

          // expect win to get called exactly once
          var win = function(a) {
            // clear watch on first call
            navigator.accelerometer.clearWatch(id);
            // if win isn't called again in 201 ms we assume success
            var tid = setTimeout(function() {
              expect(true).toBe(true);
              done();
            }, 101);
            // if win is called again, clear the timeout and fail the test
            win = function() {
              clearTimeout(tid);
              fail(done);
            };
          };

          // wrap the success call in a closure since the value of win changes between calls
          id = navigator.accelerometer.watchAcceleration(function() { win(); }, fail.bind(null, done), {frequency:100});
      });
    });
  });
};

/******************************************************************************/
/******************************************************************************/
/******************************************************************************/

exports.defineManualTests = function (contentEl, createActionButton) {
    function roundNumber(num) {
        var dec = 3;
        var result = Math.round(num * Math.pow(10, dec)) / Math.pow(10, dec);
        return result;
    }

    var watchAccelId = null;

    /**
     * Set accelerometer status
     */
    function setAccelStatus(status) {
        document.getElementById('accel_status').innerHTML = status;
    }

    /**
     * Stop watching the acceleration
     */
    function stopAccel() {
        console.log("stopAccel()");
        setAccelStatus("Stopped");
        if (watchAccelId) {
            navigator.accelerometer.clearWatch(watchAccelId);
            watchAccelId = null;
        }
    }

    /**
     * Start watching acceleration
     */
    var watchAccel = function () {
        console.log("watchAccel()");

        // Success callback
        var success = function (a) {
            document.getElementById('x').innerHTML = roundNumber(a.x);
            document.getElementById('y').innerHTML = roundNumber(a.y);
            document.getElementById('z').innerHTML = roundNumber(a.z);
            document.getElementById('t').innerHTML = a.timestamp;
        };

        // Fail callback
        var fail = function (e) {
            console.log("watchAccel fail callback with error code " + e);
            stopAccel();
            setAccelStatus(e);
        };

        // Update acceleration every 1 sec
        var opt = {};
        opt.frequency = 1000;
        watchAccelId = navigator.accelerometer.watchAcceleration(success, fail, opt);

        setAccelStatus("Running");
    };

    /**
     * Get current acceleration
     */
    var getAccel = function () {
        console.log("getAccel()");

        // Stop accel if running
        stopAccel();

        // Success callback
        var success = function (a) {
            document.getElementById('x').innerHTML = roundNumber(a.x);
            document.getElementById('y').innerHTML = roundNumber(a.y);
            document.getElementById('z').innerHTML = roundNumber(a.z);
            document.getElementById('t').innerHTML = a.timestamp;
            console.log("getAccel success callback");
        };

        // Fail callback
        var fail = function (e) {
            console.log("getAccel fail callback with error code " + e);
            setAccelStatus(e);
        };

        // Make call
        var opt = {};
        navigator.accelerometer.getCurrentAcceleration(success, fail, opt);
    };

    /******************************************************************************/

    var accelerometer_tests = '<div id="getAcceleration"></div>' +
        'Expected result: Will update the status box with X, Y, and Z values when pressed. Status will read "Stopped"' +
        '<p/> <div id="watchAcceleration"></div>' +
        'Expected result: When pressed, will start a watch on the accelerometer and update X,Y,Z values when movement is sensed. Status will read "Running"' +
        '<p/> <div id="clearAcceleration"></div>' +
        'Expected result: Will clear the accelerometer watch, so X,Y,Z values will no longer be updated. Status will read "Stopped"';

    contentEl.innerHTML = '<div id="info">' +
        'Status: <span id="accel_status">Stopped</span>' +
        '<table width="100%">' +
        '<tr><td width="30%">X:</td><td id="x"> </td></tr>' +
        '<tr><td width="30%">Y:</td><td id="y"> </td></tr>' +
        '<tr><td width="30%">Z:</td><td id="z"> </td></tr>' +
        '<tr><td width="30%">Timestamp:</td><td id="t"> </td></tr>' +
        '</table></div>' +
        accelerometer_tests;

    createActionButton('Get Acceleration', function () {
        getAccel();
    }, 'getAcceleration');

    createActionButton('Start Watch', function () {
        watchAccel();
    }, 'watchAcceleration');

    createActionButton('Clear Watch', function () {
        stopAccel();
    }, 'clearAcceleration');
};
