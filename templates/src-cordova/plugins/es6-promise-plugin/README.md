# PromisesPlugin

ES6-Promises polyfill for Cordova/PhoneGap

# Motivation

The web view components on Cordova supported platforms lack suport for ES6 Promise. A polyfill library bundled with the plugin fixes the limitation. However, as more plugin use promises, the application developer using these plugins will end up with multiple promise polyfill libraries.

This plugin attempts to fix this situation by providing a Promise polyfill so that other plugins can rely on this functionality.

# How to use

Configure your plugin's plugin.xml by adding this dependency:

```
<dependency id="es6-promise-plugin" version="4.1.0" />
```

Cordova CLI takes care to install PromisesPlugin automatically:

```
$ cordova plugins add {yourPlugin}

> Installing "{yourPlugin}" for {platform}
> Installing "es6-promise-plugin" for {platform}
```

This is all. ```window.Promise``` is available for use in your plugin.

# Credits

This plugin wraps [es6-promise](https://github.com/jakearchibald/es6-promise) in a Cordova/PhoneGap friendly way.

# License

The plugin is available under MIT license.
