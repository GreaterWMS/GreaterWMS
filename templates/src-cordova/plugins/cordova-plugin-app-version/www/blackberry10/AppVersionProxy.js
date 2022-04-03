module.exports = {
    getVersionNumber: function( success, fail ) {
        if( !blackberry || !blackberry.app || !blackberry.app.version ) {
            if( fail ) {
                return fail();
            } else {
                return "";
            }
        }

        if( success ) {
            return success( blackberry.app.version );
        }
        return blackberry.app.version;
    }
};

require("cordova/exec/proxy").add("AppVersion", module.exports);
