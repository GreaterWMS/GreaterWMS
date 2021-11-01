/*jshint node: true, jasmine: true, browser: true */
/*global ContactFindOptions, ContactName, Q*/

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

// these tests are meant to be executed by Cordova Medic Appium runner
// you can find it here: https://github.com/apache/cordova-medic/
// it is not necessary to do a full CI setup to run these tests, just run:
// node cordova-medic/medic/medic.js appium --platform android --plugins cordova-plugin-contacts

'use strict';

var wdHelper = global.WD_HELPER;
var screenshotHelper = global.SCREENSHOT_HELPER;
var contactsHelper = require('../helpers/contactsHelper');

var MINUTE = 60 * 1000;
var PLATFORM = global.PLATFORM;
var UNORM = global.UNORM;

describe('Contacts UI Automation Tests', function () {
    var driver;
    var webviewContext;
    var promiseCount = 0;
    // going to set this to false if session is created successfully
    var failedToStart = true;

    function getNextPromiseId() {
        return 'appium_promise_' + promiseCount++;
    }

    function saveScreenshotAndFail(error) {
        fail(error);
        return screenshotHelper
            .saveScreenshot(driver)
            .quit()
            .then(function () {
                return getDriver();
            });
    }

    function getDriver() {
        driver = wdHelper.getDriver(PLATFORM);
        return wdHelper.getWebviewContext(driver, 2)
            .then(function (context) {
                webviewContext = context;
                return driver.context(webviewContext);
            })
            .then(function () {
                return wdHelper.waitForDeviceReady(driver);
            })
            .then(function () {
                return wdHelper.injectLibraries(driver);
            });
    }

    function addContact(firstName, lastName, bday) {
        var bdayString = bday ? bday.toDateString() : undefined;
        var contactName = contactsHelper.getContactName(firstName, lastName);
        return driver
            .context(webviewContext)
            .setAsyncScriptTimeout(MINUTE)
            .executeAsync(function (contactname, bday, callback) {
                navigator.contacts.create({
                    'displayName': contactname.formatted,
                    'name': contactname,
                    'note': 'DeleteMe',
                    'birthday': new Date(bday)
                }).save(function (successResult) {
                    callback(successResult);
                }, function (failureResult) {
                    callback(failureResult);
                });
            }, [contactName, bdayString])
            .then(function (result) {
                if (result && result.hasOwnProperty('code')) {
                    throw result;
                }
                return result;
            });
    }

    function pickContact(name) {
        var promiseId = getNextPromiseId();
        return driver
            .context(webviewContext)
            .execute(function (pID) {
                navigator._appiumPromises[pID] = Q.defer();
                navigator.contacts.pickContact(function (contact) {
                    navigator._appiumPromises[pID].resolve(contact);
                }, function (err) {
                    navigator._appiumPromises[pID].reject(err);
                });
            }, [promiseId])
            .context('NATIVE_APP')
            .then(function () {
                switch (PLATFORM) {
                    case 'ios':
                        return driver
                            .waitForElementByAccessibilityId(name, 20000)
                            .elementByAccessibilityId(name);
                    case 'android':
                        return driver
                            .waitForElementByXPath('//android.widget.TextView[@text="' + name + '"]', MINUTE);
                }
            })
            .click()
            .context(webviewContext)
            .executeAsync(function (pID, cb) {
                navigator._appiumPromises[pID].promise
                .then(function (contact) {
                    // for some reason Appium cannot get Date object
                    // let's make birthday a string then
                    contact.birthday = contact.birthday.toDateString();
                    cb(contact);
                }, function (err) {
                    cb('ERROR: ' + err);
                });
            }, [promiseId])
            .then(function (result) {
                if (typeof result === 'string' && result.indexOf('ERROR:') === 0) {
                    throw result;
                }
                return result;
            });
    }

    function renameContact(oldName, newGivenName, newFamilyName) {
        return driver
            .context(webviewContext)
            .setAsyncScriptTimeout(7 * MINUTE)
            .executeAsync(function (oldname, newgivenname, newfamilyname, callback) {
                var obj = new ContactFindOptions();
                obj.filter = oldname;
                obj.multiple = false;

                navigator.contacts.find(['displayName', 'name'], function (contacts) {
                    if (contacts.length === 0) {
                        callback({ 'code': -35142 });
                        return;
                    }
                    var contact = contacts[0];
                    contact.displayName = newgivenname + ' ' + newfamilyname;
                    var name = new ContactName();
                    name.givenName = newgivenname;
                    name.familyName = newfamilyname;
                    contact.name = name;
                    contact.save(callback, callback);
                }, function (result) {
                    callback(result);
                }, obj);
            }, [oldName, newGivenName, newFamilyName])
            .then(function (result) {
                if (result && result.hasOwnProperty('code')) {
                    if (result.code === -35142) {
                        throw 'Couldn\'t find the contact "' + oldName + '"';
                    }
                    throw result;
                }
                return result;
            });
    }

    function removeTestContacts() {
        return driver
            .context(webviewContext)
            .setAsyncScriptTimeout(MINUTE)
            .executeAsync(function (callback) {
                var obj = new ContactFindOptions();
                obj.filter = 'DeleteMe';
                obj.multiple = true;
                navigator.contacts.find(['note'], function (contacts) {
                    var removes = [];
                    contacts.forEach(function (contact) {
                        removes.push(contact);
                    });
                    if (removes.length === 0) {
                        return;
                    }

                   var nextToRemove;
                   if (removes.length > 0) {
                        nextToRemove = removes.shift();
                    }

                    function removeNext(item) {
                        if (typeof item === 'undefined') {
                            callback();
                            return;
                        }

                        if (removes.length > 0) {
                            nextToRemove = removes.shift();
                        } else {
                            nextToRemove = undefined;
                        }

                        item.remove(function removeSucceeded() {
                            removeNext(nextToRemove);
                        }, function removeFailed() {
                            removeNext(nextToRemove);
                        });
                    }
                    removeNext(nextToRemove);
                }, function (failureResult) {
                    callback(failureResult);
                }, obj);
            }, [])
            .then(function (result) {
                if (typeof result !== 'undefined') {
                    throw result;
                }
            });
    }

    function checkSession(done) {
        if (failedToStart) {
            fail('Failed to start a session');
            done();
        }
    }

    afterAll(function (done) {
        checkSession(done);
        driver
            .quit()
            .done(done);
    }, MINUTE);

    it('should connect to an appium endpoint properly', function (done) {
        // retry up to 3 times
        getDriver()
            .fail(function () {
                return getDriver()
                    .fail(function () {
                        return getDriver()
                            .fail(fail);
                    });
            })
            .then(function () {
                failedToStart = false;
            }, fail)
            .then(function () {
                // on iOS and Android >= 6, first interaction with contacts API will trigger the permission dialog.
                // We will attempt to bust it manually here, by triggering the contacts API
                // and waiting for the native dialog to show up, then dismissing the alert.
                // This only needs to be done once.
                // NOTE: in earlier versions of iOS (9.3 and below), using the older UI testing library
                // (UIAutomation), Appium's autoAcceptAlerts capability handles this for us. This logic
                // is here as a transition between UIAutomation and XCUITest and is compatible with both.
                // More details in the comment below.
                var promiseId = getNextPromiseId();
                var contactName = contactsHelper.getContactName('Permission', 'Buster');
                return driver
                    .context(webviewContext)
                    .execute(function (pID, contactname) {
                        navigator._appiumPromises[pID] = Q.defer();
                        navigator.contacts.create({
                            'displayName': contactname.formatted,
                            'name': contactname,
                            'note': 'DeleteMe'
                        }).save(function (contact) {
                            navigator._appiumPromises[pID].resolve(contact);
                        }, function (err) {
                            navigator._appiumPromises[pID].reject(err);
                        });
                    }, [promiseId, contactName])
                    .context('NATIVE_APP')
                    .then(function () {
                        // iOS
                        if (PLATFORM === 'ios') {
                            return driver.acceptAlert()
                                .then(function alertDismissed() {
                                    // TODO: once we move to only XCUITest-based (which is force on you in either iOS 10+ or Xcode 8+)
                                    // UI tests, we will have to:
                                    // a) remove use of autoAcceptAlerts appium capability since it no longer functions in XCUITest
                                    // b) can remove this entire then() clause, as we do not need to explicitly handle the acceptAlert
                                    //    failure callback, since we will be guaranteed to hit the permission dialog on startup.
                                 }, function noAlert() {
                                     // in case the contacts permission alert never showed up: no problem, don't freak out.
                                     // This can happen if:
                                     // a) The application-under-test already had contacts permissions granted to it
                                     // b) Appium's autoAcceptAlerts capability is provided (and functioning)
                                 });
                        }

                        // Android
                        return driver
                            .elementByXPath('//android.widget.Button[translate(@text, "alow", "ALOW")="ALLOW"]')
                            .click()
                            .fail(function noAlert() { });
                    })
                    .context(webviewContext)
                    .executeAsync(function (pID, cb) {
                        navigator._appiumPromises[pID].promise
                            .then(function (result) {
                                cb(result);
                            }, function (err) {
                                cb('ERROR: ' + err);
                            });
                    }, [promiseId])
                    .then(function (result) {
                        if (typeof result === 'string' && result.indexOf('ERROR:') === 0) {
                            throw result;
                        }
                        return result;
                    });
            })
            .done(done);
    }, 30 * MINUTE);

    describe('Picking contacts', function () {
        afterEach(function (done) {
            checkSession(done);
            removeTestContacts()
                .finally(done);
        }, MINUTE);

        it('contacts.ui.spec.1 Pick a contact', function (done) {
            checkSession(done);
            var bday = new Date(1991, 1, 1);
            driver
                .then(function () {
                    return addContact('Test', 'Contact', bday);
                })
                .then(function () {
                    return pickContact('Test Contact');
                })
                .then(function (contact) {
                    expect(contact.name.givenName).toBe('Test');
                    expect(contact.name.familyName).toBe('Contact');
                    expect(contact.birthday).toBe(bday.toDateString());
                })
                .fail(saveScreenshotAndFail)
                .done(done);
        }, 5 * MINUTE);

        it('contacts.ui.spec.2 Update an existing contact', function (done) {
            checkSession(done);
            driver
                .then(function () {
                    return addContact('Dooney', 'Evans');
                })
                .then(function () {
                    return renameContact('Dooney Evans', 'Urist', 'McContact');
                })
                .then(function () {
                    return pickContact('Urist McContact');
                })
                .then(function (contact) {
                    expect(contact.name.givenName).toBe('Urist');
                    expect(contact.name.familyName).toBe('McContact');
                })
                .fail(saveScreenshotAndFail)
                .done(done);
        }, 10 * MINUTE);

        it('contacts.ui.spec.3 Create a contact with no name', function (done) {
            checkSession(done);
            driver
                .then(function () {
                    return addContact();
                })
                .then(function () {
                    switch (PLATFORM) {
                        case 'android':
                            return pickContact('(No name)');
                        case 'ios':
                            return pickContact('No Name');
                    }
                })
                .then(function (contact) {
                    if (contact.name) {
                        expect(contact.name.givenName).toBeFalsy();
                        expect(contact.name.middleName).toBeFalsy();
                        expect(contact.name.familyName).toBeFalsy();
                        expect(contact.name.formatted).toBeFalsy();
                    } else {
                        expect(contact.name).toBeFalsy();
                    }
                })
                .fail(saveScreenshotAndFail)
                .done(done);
        }, 5 * MINUTE);

        it('contacts.ui.spec.4 Create a contact with Unicode characters in name', function (done) {
            checkSession(done);
            driver
                .then(function () {
                    return addContact('Н€йромонах', 'ФеофаЊ');
                })
                .then(function () {
                    return pickContact('Н€йромонах ФеофаЊ');
                })
                .then(function (contact) {
                    expect(contact.name.givenName).toBe('Н€йромонах');
                    expect(contact.name.familyName).toBe('ФеофаЊ');
                })
                .fail(saveScreenshotAndFail)
                .done(done);
        }, 5 * MINUTE);
    });
});
