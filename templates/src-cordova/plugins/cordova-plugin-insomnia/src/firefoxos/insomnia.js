var lock;

module.exports = {
    keepAwake: function() {
        if (navigator.requestWakeLock) {
            lock = navigator.requestWakeLock("screen");
        }
    },
    allowSleepAgain: function() {
        if (lock && typeof lock.unlock === "function") {
            lock.unlock();
        }
    }
};

require("cordova/exec/proxy").add("Insomnia", module.exports);
