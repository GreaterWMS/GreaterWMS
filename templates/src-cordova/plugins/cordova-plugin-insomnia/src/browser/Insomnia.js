function notSupported() {
    console.log('Insomnia is not supported on the browser');
}

module.exports = {
    keepAwake: notSupported,
    allowSleepAgain: notSupported
};

require('cordova/exec/proxy').add('Insomnia', module.exports);
