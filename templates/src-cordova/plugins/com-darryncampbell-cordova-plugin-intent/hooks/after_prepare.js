const fs = require("fs");

function androidXUpgrade (ctx) {
    if (!ctx.opts.platforms.includes('android'))
        return;

    const enableAndroidX = "android.useAndroidX=true";
    const enableJetifier = "android.enableJetifier=true";
    const gradlePropertiesPath = "./platforms/android/gradle.properties";

    let gradleProperties = fs.readFileSync(gradlePropertiesPath, "utf8");

    if (gradleProperties)
    {
        const isAndroidXEnabled = gradleProperties.includes(enableAndroidX);
        const isJetifierEnabled = gradleProperties.includes(enableJetifier);

        if (isAndroidXEnabled && isJetifierEnabled)
            return;

        if (isAndroidXEnabled === false)
            gradleProperties += "\n" + enableAndroidX;

        if (isJetifierEnabled === false)
            gradleProperties += "\n" + enableJetifier;

        fs.writeFileSync(gradlePropertiesPath, gradleProperties);
    }
}

module.exports = function (ctx) {
    androidXUpgrade(ctx);
};
