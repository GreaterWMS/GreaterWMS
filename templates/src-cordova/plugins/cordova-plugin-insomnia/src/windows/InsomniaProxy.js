
var displayRequest = null;

var handleAsyncError = function(handler,msg) {
    setTimeout(function(){
        handler(msg);
    },0);
};

module.exports = {
    
    keepAwake:function(success,error){
        if(!displayRequest) {
            try {
                displayRequest = new Windows.System.Display.DisplayRequest();
                displayRequest.requestActive();
                setTimeout(function(){
                    success();
                },0);
            }
            catch(err) {
                handleAsyncError(error,"Insomnia failed to activate display request : " + err.message);
            }
        }
        else {
            handleAsyncError(error,"Insomnia is wide awake!");
        }
    },
    allowSleepAgain:function(success,error){
        if(displayRequest) {
            try {
                displayRequest.requestRelease();
                displayRequest = null;
                setTimeout(function(){
                    success();
                },0);
            }
            catch(err) {
                handleAsyncError(error,"Insomnia failed to deactivate display request : " + err.message);
            }
        }
        else {
            handleAsyncError(error,"Insomnia is already asleep!");
        }
    }
};

require("cordova/exec/proxy").add("Insomnia", module.exports);