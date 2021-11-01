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

/* global unescape */

(function (window, undefined) { // eslint-disable-line no-shadow-restricted-names
    'use strict';

    /* jshint validthis:true */
    function L10nError (message, id, loc) {
        this.name = 'L10nError';
        this.message = message;
        this.id = id;
        this.loc = loc;
    }
    L10nError.prototype = Object.create(Error.prototype);
    L10nError.prototype.constructor = L10nError;

    /* jshint browser:true */

    var io = {
        load: function load (url, callback, sync) {
            var xhr = new XMLHttpRequest(); // eslint-disable-line no-undef

            if (xhr.overrideMimeType) {
                xhr.overrideMimeType('text/plain');
            }

            xhr.open('GET', url, !sync);

            xhr.addEventListener('load', function io_load (e) {
                if (e.target.status === 200 || e.target.status === 0) {
                    callback(null, e.target.responseText);
                } else {
                    callback(new L10nError('Not found: ' + url));
                }
            });
            xhr.addEventListener('error', callback);
            xhr.addEventListener('timeout', callback);

            // the app: protocol throws on 404, see https://bugzil.la/827243
            try {
                xhr.send(null);
            } catch (e) {
                callback(new L10nError('Not found: ' + url));
            }
        },

        loadJSON: function loadJSON (url, callback) {
            var xhr = new XMLHttpRequest(); // eslint-disable-line no-undef

            if (xhr.overrideMimeType) {
                xhr.overrideMimeType('application/json');
            }

            xhr.open('GET', url);

            xhr.responseType = 'json';
            xhr.addEventListener('load', function io_loadjson (e) {
                if (e.target.status === 200 || e.target.status === 0) {
                    callback(null, e.target.response);
                } else {
                    callback(new L10nError('Not found: ' + url));
                }
            });
            xhr.addEventListener('error', callback);
            xhr.addEventListener('timeout', callback);

            // the app: protocol throws on 404, see https://bugzil.la/827243
            try {
                xhr.send(null);
            } catch (e) {
                callback(new L10nError('Not found: ' + url));
            }
        }
    };

    function EventEmitter () {}

    EventEmitter.prototype.emit = function ee_emit () {
        if (!this._listeners) {
            return;
        }

        var args = Array.prototype.slice.call(arguments);
        var type = args.shift();
        if (!this._listeners[type]) {
            return;
        }

        var typeListeners = this._listeners[type].slice();
        for (var i = 0; i < typeListeners.length; i++) {
            typeListeners[i].apply(this, args);
        }
    };

    EventEmitter.prototype.addEventListener = function ee_add (type, listener) {
        if (!this._listeners) {
            this._listeners = {};
        }
        if (!(type in this._listeners)) {
            this._listeners[type] = [];
        }
        this._listeners[type].push(listener);
    };

    EventEmitter.prototype.removeEventListener = function ee_rm (type, listener) {
        if (!this._listeners) {
            return;
        }

        var typeListeners = this._listeners[type];
        var pos = typeListeners.indexOf(listener);
        if (pos === -1) {
            return;
        }

        typeListeners.splice(pos, 1);
    };

    function getPluralRule (lang) {
        var locales2rules = {
            'af': 3,
            'ak': 4,
            'am': 4,
            'ar': 1,
            'asa': 3,
            'az': 0,
            'be': 11,
            'bem': 3,
            'bez': 3,
            'bg': 3,
            'bh': 4,
            'bm': 0,
            'bn': 3,
            'bo': 0,
            'br': 20,
            'brx': 3,
            'bs': 11,
            'ca': 3,
            'cgg': 3,
            'chr': 3,
            'cs': 12,
            'cy': 17,
            'da': 3,
            'de': 3,
            'dv': 3,
            'dz': 0,
            'ee': 3,
            'el': 3,
            'en': 3,
            'eo': 3,
            'es': 3,
            'et': 3,
            'eu': 3,
            'fa': 0,
            'ff': 5,
            'fi': 3,
            'fil': 4,
            'fo': 3,
            'fr': 5,
            'fur': 3,
            'fy': 3,
            'ga': 8,
            'gd': 24,
            'gl': 3,
            'gsw': 3,
            'gu': 3,
            'guw': 4,
            'gv': 23,
            'ha': 3,
            'haw': 3,
            'he': 2,
            'hi': 4,
            'hr': 11,
            'hu': 0,
            'id': 0,
            'ig': 0,
            'ii': 0,
            'is': 3,
            'it': 3,
            'iu': 7,
            'ja': 0,
            'jmc': 3,
            'jv': 0,
            'ka': 0,
            'kab': 5,
            'kaj': 3,
            'kcg': 3,
            'kde': 0,
            'kea': 0,
            'kk': 3,
            'kl': 3,
            'km': 0,
            'kn': 0,
            'ko': 0,
            'ksb': 3,
            'ksh': 21,
            'ku': 3,
            'kw': 7,
            'lag': 18,
            'lb': 3,
            'lg': 3,
            'ln': 4,
            'lo': 0,
            'lt': 10,
            'lv': 6,
            'mas': 3,
            'mg': 4,
            'mk': 16,
            'ml': 3,
            'mn': 3,
            'mo': 9,
            'mr': 3,
            'ms': 0,
            'mt': 15,
            'my': 0,
            'nah': 3,
            'naq': 7,
            'nb': 3,
            'nd': 3,
            'ne': 3,
            'nl': 3,
            'nn': 3,
            'no': 3,
            'nr': 3,
            'nso': 4,
            'ny': 3,
            'nyn': 3,
            'om': 3,
            'or': 3,
            'pa': 3,
            'pap': 3,
            'pl': 13,
            'ps': 3,
            'pt': 3,
            'rm': 3,
            'ro': 9,
            'rof': 3,
            'ru': 11,
            'rwk': 3,
            'sah': 0,
            'saq': 3,
            'se': 7,
            'seh': 3,
            'ses': 0,
            'sg': 0,
            'sh': 11,
            'shi': 19,
            'sk': 12,
            'sl': 14,
            'sma': 7,
            'smi': 7,
            'smj': 7,
            'smn': 7,
            'sms': 7,
            'sn': 3,
            'so': 3,
            'sq': 3,
            'sr': 11,
            'ss': 3,
            'ssy': 3,
            'st': 3,
            'sv': 3,
            'sw': 3,
            'syr': 3,
            'ta': 3,
            'te': 3,
            'teo': 3,
            'th': 0,
            'ti': 4,
            'tig': 3,
            'tk': 3,
            'tl': 4,
            'tn': 3,
            'to': 0,
            'tr': 0,
            'ts': 3,
            'tzm': 22,
            'uk': 11,
            'ur': 3,
            've': 3,
            'vi': 0,
            'vun': 3,
            'wa': 4,
            'wae': 3,
            'wo': 0,
            'xh': 3,
            'xog': 3,
            'yo': 0,
            'zh': 0,
            'zu': 3
        };

        // utility functions for plural rules methods
        function isIn (n, list) {
            return list.indexOf(n) !== -1;
        }
        function isBetween (n, start, end) {
            return typeof n === typeof start && start <= n && n <= end;
        }

        // list of all plural rules methods:
        // map an integer to the plural form name to use
        var pluralRules = {
            '0': function () {
                return 'other';
            },
            '1': function (n) {
                if ((isBetween((n % 100), 3, 10))) {
                    return 'few';
                }
                if (n === 0) {
                    return 'zero';
                }
                if ((isBetween((n % 100), 11, 99))) {
                    return 'many';
                }
                if (n === 2) {
                    return 'two';
                }
                if (n === 1) {
                    return 'one';
                }
                return 'other';
            },
            '2': function (n) {
                if (n !== 0 && (n % 10) === 0) {
                    return 'many';
                }
                if (n === 2) {
                    return 'two';
                }
                if (n === 1) {
                    return 'one';
                }
                return 'other';
            },
            '3': function (n) {
                if (n === 1) {
                    return 'one';
                }
                return 'other';
            },
            '4': function (n) {
                if ((isBetween(n, 0, 1))) {
                    return 'one';
                }
                return 'other';
            },
            '5': function (n) {
                if ((isBetween(n, 0, 2)) && n !== 2) {
                    return 'one';
                }
                return 'other';
            },
            '6': function (n) {
                if (n === 0) {
                    return 'zero';
                }
                if ((n % 10) === 1 && (n % 100) !== 11) {
                    return 'one';
                }
                return 'other';
            },
            '7': function (n) {
                if (n === 2) {
                    return 'two';
                }
                if (n === 1) {
                    return 'one';
                }
                return 'other';
            },
            '8': function (n) {
                if ((isBetween(n, 3, 6))) {
                    return 'few';
                }
                if ((isBetween(n, 7, 10))) {
                    return 'many';
                }
                if (n === 2) {
                    return 'two';
                }
                if (n === 1) {
                    return 'one';
                }
                return 'other';
            },
            '9': function (n) {
                if ((n === 0 || n !== 1) && (isBetween((n % 100), 1, 19))) {
                    return 'few';
                }
                if (n === 1) {
                    return 'one';
                }
                return 'other';
            },
            '10': function (n) {
                if ((isBetween((n % 10), 2, 9)) && !(isBetween((n % 100), 11, 19))) {
                    return 'few';
                }
                if ((n % 10) === 1 && !(isBetween((n % 100), 11, 19))) {
                    return 'one';
                }
                return 'other';
            },
            '11': function (n) {
                if ((isBetween((n % 10), 2, 4)) && !(isBetween((n % 100), 12, 14))) {
                    return 'few';
                }
                if ((n % 10) === 0 ||
            (isBetween((n % 10), 5, 9)) ||
            (isBetween((n % 100), 11, 14))) {
                    return 'many';
                }
                if ((n % 10) === 1 && (n % 100) !== 11) {
                    return 'one';
                }
                return 'other';
            },
            '12': function (n) {
                if ((isBetween(n, 2, 4))) {
                    return 'few';
                }
                if (n === 1) {
                    return 'one';
                }
                return 'other';
            },
            '13': function (n) {
                if ((isBetween((n % 10), 2, 4)) && !(isBetween((n % 100), 12, 14))) {
                    return 'few';
                }
                if ((n !== 1 && (isBetween((n % 10), 0, 1))) ||
            ((isBetween((n % 10), 5, 9))) ||
            ((isBetween((n % 100), 12, 14)))) {
                    return 'many';
                }
                if (n === 1) {
                    return 'one';
                }
                return 'other';
            },
            '14': function (n) {
                if ((isBetween((n % 100), 3, 4))) {
                    return 'few';
                }
                if ((n % 100) === 2) {
                    return 'two';
                }
                if ((n % 100) === 1) {
                    return 'one';
                }
                return 'other';
            },
            '15': function (n) {
                if (n === 0 || (isBetween((n % 100), 2, 10))) {
                    return 'few';
                }
                if ((isBetween((n % 100), 11, 19))) {
                    return 'many';
                }
                if (n === 1) {
                    return 'one';
                }
                return 'other';
            },
            '16': function (n) {
                if ((n % 10) === 1 && n !== 11) {
                    return 'one';
                }
                return 'other';
            },
            '17': function (n) {
                if (n === 3) {
                    return 'few';
                }
                if (n === 0) {
                    return 'zero';
                }
                if (n === 6) {
                    return 'many';
                }
                if (n === 2) {
                    return 'two';
                }
                if (n === 1) {
                    return 'one';
                }
                return 'other';
            },
            '18': function (n) {
                if (n === 0) {
                    return 'zero';
                }
                if ((isBetween(n, 0, 2)) && n !== 0 && n !== 2) {
                    return 'one';
                }
                return 'other';
            },
            '19': function (n) {
                if ((isBetween(n, 2, 10))) {
                    return 'few';
                }
                if ((isBetween(n, 0, 1))) {
                    return 'one';
                }
                return 'other';
            },
            '20': function (n) {
                if ((isBetween((n % 10), 3, 4) || ((n % 10) === 9)) && !(
                    isBetween((n % 100), 10, 19) ||
                    isBetween((n % 100), 70, 79) ||
                    isBetween((n % 100), 90, 99)
                )) {
                    return 'few';
                }
                if ((n % 1000000) === 0 && n !== 0) {
                    return 'many';
                }
                if ((n % 10) === 2 && !isIn((n % 100), [12, 72, 92])) {
                    return 'two';
                }
                if ((n % 10) === 1 && !isIn((n % 100), [11, 71, 91])) {
                    return 'one';
                }
                return 'other';
            },
            '21': function (n) {
                if (n === 0) {
                    return 'zero';
                }
                if (n === 1) {
                    return 'one';
                }
                return 'other';
            },
            '22': function (n) {
                if ((isBetween(n, 0, 1)) || (isBetween(n, 11, 99))) {
                    return 'one';
                }
                return 'other';
            },
            '23': function (n) {
                if ((isBetween((n % 10), 1, 2)) || (n % 20) === 0) {
                    return 'one';
                }
                return 'other';
            },
            '24': function (n) {
                if ((isBetween(n, 3, 10) || isBetween(n, 13, 19))) {
                    return 'few';
                }
                if (isIn(n, [2, 12])) {
                    return 'two';
                }
                if (isIn(n, [1, 11])) {
                    return 'one';
                }
                return 'other';
            }
        };

        // return a function that gives the plural form name for a given integer
        var index = locales2rules[lang.replace(/-.*$/, '')];
        if (!(index in pluralRules)) {
            return function () { return 'other'; };
        }
        return pluralRules[index];
    }

    var parsePatterns;

    function parse (ctx, source) {
        var ast = {};
        /* eslint-disable no-useless-escape */
        if (!parsePatterns) {
            parsePatterns = {
                comment: /^\s*#|^\s*$/,
                entity: /^([^=\s]+)\s*=\s*(.+)$/,
                multiline: /[^\\]\\$/,
                macro: /\{\[\s*(\w+)\(([^\)]*)\)\s*\]\}/i,
                unicode: /\\u([0-9a-fA-F]{1,4})/g,
                entries: /[\r\n]+/,
                controlChars: /\\([\\\n\r\t\b\f\{\}\"\'])/g
            };
        }
        /* eslint-enable no-useless-escape */
        var entries = source.split(parsePatterns.entries);
        for (var i = 0; i < entries.length; i++) {
            var line = entries[i];

            if (parsePatterns.comment.test(line)) {
                continue;
            }

            while (parsePatterns.multiline.test(line) && i < entries.length) {
                line = line.slice(0, -1) + entries[++i].trim();
            }

            var entityMatch = line.match(parsePatterns.entity);
            if (entityMatch) {
                try {
                    parseEntity(entityMatch[1], entityMatch[2], ast);
                } catch (e) {
                    if (ctx) {
                        ctx._emitter.emit('error', e);
                    } else {
                        throw e;
                    }
                }
            }
        }
        return ast;
    }

    function setEntityValue (id, attr, key, value, ast) {
        var obj = ast;
        var prop = id;

        if (attr) {
            if (!(id in obj)) {
                obj[id] = {};
            }
            if (typeof (obj[id]) === 'string') {
                obj[id] = {'_': obj[id]};
            }
            obj = obj[id];
            prop = attr;
        }

        if (!key) {
            obj[prop] = value;
            return;
        }

        if (!(prop in obj)) {
            obj[prop] = {'_': {}};
        } else if (typeof (obj[prop]) === 'string') {
            obj[prop] = {'_index': parseMacro(obj[prop]), '_': {}};
        }
        obj[prop]._[key] = value;
    }

    function parseEntity (id, value, ast) {
        var name, key;

        var pos = id.indexOf('[');
        if (pos !== -1) {
            name = id.substr(0, pos);
            key = id.substring(pos + 1, id.length - 1);
        } else {
            name = id;
            key = null;
        }

        var nameElements = name.split('.');

        if (nameElements.length > 2) {
            throw new Error('Error in ID: "' + name + '".' +
                      ' Nested attributes are not supported.');
        }

        var attr;
        if (nameElements.length > 1) {
            name = nameElements[0];
            attr = nameElements[1];
        } else {
            attr = null;
        }

        setEntityValue(name, attr, key, unescapeString(value), ast);
    }

    function unescapeControlCharacters (str) {
        return str.replace(parsePatterns.controlChars, '$1');
    }

    function unescapeUnicode (str) {
        return str.replace(parsePatterns.unicode, function (match, token) {
            return unescape('%u' + '0000'.slice(token.length) + token);
        });
    }

    function unescapeString (str) {
        if (str.lastIndexOf('\\') !== -1) {
            str = unescapeControlCharacters(str);
        }
        return unescapeUnicode(str);
    }

    function parseMacro (str) {
        var match = str.match(parsePatterns.macro);
        if (!match) {
            throw new L10nError('Malformed macro');
        }
        return [match[1], match[2]];
    }

    var MAX_PLACEABLE_LENGTH = 2500;
    var MAX_PLACEABLES = 100;
    var rePlaceables = /\{\{\s*(.+?)\s*\}\}/g;

    function Entity (id, node, env) {
        this.id = id;
        this.env = env;
        // the dirty guard prevents cyclic or recursive references from other
        // Entities; see Entity.prototype.resolve
        this.dirty = false;
        if (typeof node === 'string') {
            this.value = node;
        } else {
            // it's either a hash or it has attrs, or both
            for (var key in node) {
                if (node.hasOwnProperty(key) && key[0] !== '_') {
                    if (!this.attributes) {
                        this.attributes = {};
                    }
                    this.attributes[key] = new Entity(this.id + '.' + key, node[key],
                        env);
                }
            }
            this.value = node._ || null;
            this.index = node._index;
        }
    }

    Entity.prototype.resolve = function E_resolve (ctxdata) {
        if (this.dirty) {
            return undefined;
        }

        this.dirty = true;
        var val;
        // if resolve fails, we want the exception to bubble up and stop the whole
        // resolving process;  however, we still need to clean up the dirty flag
        try {
            val = resolve(ctxdata, this.env, this.value, this.index);
        } finally {
            this.dirty = false;
        }
        return val;
    };

    Entity.prototype.toString = function E_toString (ctxdata) {
        try {
            return this.resolve(ctxdata);
        } catch (e) {
            return undefined;
        }
    };

    Entity.prototype.valueOf = function E_valueOf (ctxdata) {
        if (!this.attributes) {
            return this.toString(ctxdata);
        }

        var entity = {
            value: this.toString(ctxdata),
            attributes: {}
        };

        for (var key in this.attributes) {
            if (this.attributes.hasOwnProperty(key)) {
                entity.attributes[key] = this.attributes[key].toString(ctxdata);
            }
        }

        return entity;
    };

    function subPlaceable (ctxdata, env, match, id) {
        if (ctxdata && ctxdata.hasOwnProperty(id) &&
        (typeof ctxdata[id] === 'string' ||
         (typeof ctxdata[id] === 'number' && !isNaN(ctxdata[id])))) {
            return ctxdata[id];
        }

        if (env.hasOwnProperty(id)) {
            if (!(env[id] instanceof Entity)) {
                env[id] = new Entity(id, env[id], env);
            }
            var value = env[id].resolve(ctxdata);
            if (typeof value === 'string') {
                // prevent Billion Laughs attacks
                if (value.length >= MAX_PLACEABLE_LENGTH) {
                    throw new L10nError('Too many characters in placeable (' +
                              value.length + ', max allowed is ' +
                              MAX_PLACEABLE_LENGTH + ')');
                }
                return value;
            }
        }
        return match;
    }

    function interpolate (ctxdata, env, str) {
        var placeablesCount = 0;
        var value = str.replace(rePlaceables, function (match, id) {
            // prevent Quadratic Blowup attacks
            if (placeablesCount++ >= MAX_PLACEABLES) {
                throw new L10nError('Too many placeables (' + placeablesCount +
                            ', max allowed is ' + MAX_PLACEABLES + ')');
            }
            return subPlaceable(ctxdata, env, match, id);
        });
        placeablesCount = 0;
        return value;
    }

    function resolve (ctxdata, env, expr, index) {
        if (typeof expr === 'string') {
            return interpolate(ctxdata, env, expr);
        }

        if (typeof expr === 'boolean' ||
        typeof expr === 'number' ||
        !expr) {
            return expr;
        }

        // otherwise, it's a dict

        if (index && ctxdata && ctxdata.hasOwnProperty(index[1])) {
            var argValue = ctxdata[index[1]];

            // special cases for zero, one, two if they are defined on the hash
            if (argValue === 0 && 'zero' in expr) {
                return resolve(ctxdata, env, expr.zero);
            }
            if (argValue === 1 && 'one' in expr) {
                return resolve(ctxdata, env, expr.one);
            }
            if (argValue === 2 && 'two' in expr) {
                return resolve(ctxdata, env, expr.two);
            }

            var selector = env.__plural(argValue);
            if (expr.hasOwnProperty(selector)) {
                return resolve(ctxdata, env, expr[selector]);
            }
        }

        // if there was no index or no selector was found, try 'other'
        if ('other' in expr) {
            return resolve(ctxdata, env, expr.other);
        }

        return undefined;
    }

    function compile (env, ast) {
        env = env || {};
        for (var id in ast) {
            if (ast.hasOwnProperty(id)) {
                env[id] = new Entity(id, ast[id], env);
            }
        }
        return env;
    }

    function Locale (id, ctx) {
        this.id = id;
        this.ctx = ctx;
        this.isReady = false;
        this.entries = {
            __plural: getPluralRule(id)
        };
    }

    Locale.prototype.getEntry = function L_getEntry (id) {

        var entries = this.entries;

        if (!entries.hasOwnProperty(id)) {
            return undefined;
        }

        if (entries[id] instanceof Entity) {
            return entries[id];
        }

        return entries[id] = new Entity(id, entries[id], entries); // eslint-disable-line no-return-assign
    };

    Locale.prototype.build = function L_build (callback) {
        var sync = !callback;
        var ctx = this.ctx;
        var self = this;

        var l10nLoads = ctx.resLinks.length;

        function onL10nLoaded (err) {
            if (err) {
                ctx._emitter.emit('error', err);
            }
            if (--l10nLoads <= 0) {
                self.isReady = true;
                if (callback) {
                    callback();
                }
            }
        }

        if (l10nLoads === 0) {
            onL10nLoaded();
            return;
        }

        function onJSONLoaded (err, json) {
            if (!err && json) {
                self.addAST(json);
            }
            onL10nLoaded(err);
        }

        function onPropLoaded (err, source) {
            if (!err && source) {
                var ast = parse(ctx, source);
                self.addAST(ast);
            }
            onL10nLoaded(err);
        }

        for (var i = 0; i < ctx.resLinks.length; i++) {
            var path = ctx.resLinks[i].replace('{{locale}}', this.id);
            var type = path.substr(path.lastIndexOf('.') + 1);

            switch (type) {
            case 'json':
                io.loadJSON(path, onJSONLoaded, sync);
                break;
            case 'properties':
                io.load(path, onPropLoaded, sync);
                break;
            }
        }
    };

    Locale.prototype.addAST = function (ast) {
        for (var id in ast) {
            if (ast.hasOwnProperty(id)) {
                this.entries[id] = ast[id];
            }
        }
    };

    Locale.prototype.getEntity = function (id, ctxdata) {
        var entry = this.getEntry(id);

        if (!entry) {
            return null;
        }
        return entry.valueOf(ctxdata);
    };

    function Context (id) {

        this.id = id;
        this.isReady = false;
        this.isLoading = false;

        this.supportedLocales = [];
        this.resLinks = [];
        this.locales = {};

        this._emitter = new EventEmitter();

        // Getting translations

        function getWithFallback (id) {

            if (!this.isReady) {
                throw new L10nError('Context not ready');
            }

            var cur = 0;
            var loc;
            var locale;
            while (loc = this.supportedLocales[cur]) { // eslint-disable-line no-cond-assign
                locale = this.getLocale(loc);
                if (!locale.isReady) {
                    // build without callback, synchronously
                    locale.build(null);
                }
                var entry = locale.getEntry(id);
                if (entry === undefined) {
                    cur++;
                    warning.call(this, new L10nError(id + ' not found in ' + loc, id,
                        loc));
                    continue;
                }
                return entry;
            }

            error.call(this, new L10nError(id + ' not found', id));
            return null;
        }

        this.get = function get (id, ctxdata) {
            var entry = getWithFallback.call(this, id);
            if (entry === null) {
                return '';
            }

            return entry.toString(ctxdata) || '';
        };

        this.getEntity = function getEntity (id, ctxdata) {
            var entry = getWithFallback.call(this, id);
            if (entry === null) {
                return null;
            }

            return entry.valueOf(ctxdata);
        };

        // Helpers

        this.getLocale = function getLocale (code) {

            var locales = this.locales;
            if (locales[code]) {
                return locales[code];
            }

            return locales[code] = new Locale(code, this); // eslint-disable-line no-return-assign
        };

        // Getting ready

        function negotiate (available, requested, defaultLocale) {
            if (available.indexOf(requested[0]) === -1 ||
          requested[0] === defaultLocale) {
                return [defaultLocale];
            } else {
                return [requested[0], defaultLocale];
            }
        }

        function freeze (supported) {
            var locale = this.getLocale(supported[0]);
            if (locale.isReady) {
                setReady.call(this, supported);
            } else {
                locale.build(setReady.bind(this, supported));
            }
        }

        function setReady (supported) {
            this.supportedLocales = supported;
            this.isReady = true;
            this._emitter.emit('ready');
        }

        this.requestLocales = function requestLocales () {
            if (this.isLoading && !this.isReady) {
                throw new L10nError('Context not ready');
            }

            this.isLoading = true;
            var requested = Array.prototype.slice.call(arguments);

            var supported = negotiate(requested.concat('en-US'), requested, 'en-US');
            freeze.call(this, supported);
        };

        // Events

        this.addEventListener = function addEventListener (type, listener) {
            this._emitter.addEventListener(type, listener);
        };

        this.removeEventListener = function removeEventListener (type, listener) {
            this._emitter.removeEventListener(type, listener);
        };

        this.ready = function ready (callback) {
            if (this.isReady) {
                setTimeout(callback);
            }
            this.addEventListener('ready', callback);
        };

        this.once = function once (callback) {
            if (this.isReady) {
                setTimeout(callback);
                return;
            }

            var callAndRemove = function () {
                this.removeEventListener('ready', callAndRemove);
                callback();
            }.bind(this);
            this.addEventListener('ready', callAndRemove);
        };

        // Errors

        function warning (e) {
            this._emitter.emit('warning', e);
            return e;
        }

        function error (e) {
            this._emitter.emit('error', e);
            return e;
        }
    }

    var DEBUG = false;
    var isPretranslated = false;
    var rtlList = ['ar', 'he', 'fa', 'ps', 'qps-plocm', 'ur'];
    var nodeObserver = false;

    var moConfig = {
        attributes: true,
        characterData: false,
        childList: true,
        subtree: true,
        attributeFilter: ['data-l10n-id', 'data-l10n-args']
    };

    // Public API

    navigator.mozL10n = {
        ctx: new Context(),
        get: function get (id, ctxdata) {
            return navigator.mozL10n.ctx.get(id, ctxdata);
        },
        localize: function localize (element, id, args) {
            return localizeElement.call(navigator.mozL10n, element, id, args);
        },
        translate: function () {
        // XXX: Remove after removing obsolete calls. Bugs 992473 and 1020136
        },
        translateFragment: function (fragment) {
            return translateFragment.call(navigator.mozL10n, fragment);
        },
        setAttributes: setL10nAttributes,
        getAttributes: getL10nAttributes,
        ready: function ready (callback) {
            return navigator.mozL10n.ctx.ready(callback);
        },
        once: function once (callback) {
            return navigator.mozL10n.ctx.once(callback);
        },
        get readyState () {
            return navigator.mozL10n.ctx.isReady ? 'complete' : 'loading';
        },
        language: {
            set code (lang) {
                navigator.mozL10n.ctx.requestLocales(lang);
            },
            get code () {
                return navigator.mozL10n.ctx.supportedLocales[0];
            },
            get direction () {
                return getDirection(navigator.mozL10n.ctx.supportedLocales[0]);
            }
        },
        _getInternalAPI: function () {
            return {
                Error: L10nError,
                Context: Context,
                Locale: Locale,
                Entity: Entity,
                getPluralRule: getPluralRule,
                rePlaceables: rePlaceables,
                getTranslatableChildren: getTranslatableChildren,
                translateDocument: translateDocument,
                loadINI: loadINI,
                fireLocalizedEvent: fireLocalizedEvent,
                parse: parse,
                compile: compile
            };
        }
    };

    navigator.mozL10n.ctx.ready(onReady.bind(navigator.mozL10n));

    if (DEBUG) {
        navigator.mozL10n.ctx.addEventListener('error', console.error);
        navigator.mozL10n.ctx.addEventListener('warning', console.warn);
    }

    function getDirection (lang) {
        return (rtlList.indexOf(lang) >= 0) ? 'rtl' : 'ltr';
    }

    var readyStates = {
        'loading': 0,
        'interactive': 1,
        'complete': 2
    };

    function waitFor (state, callback) {
        state = readyStates[state];
        if (readyStates[document.readyState] >= state) {
            callback();
            return;
        }

        document.addEventListener('readystatechange', function l10n_onrsc () {
            if (readyStates[document.readyState] >= state) {
                document.removeEventListener('readystatechange', l10n_onrsc);
                callback();
            }
        });
    }

    if (window.document) {
        isPretranslated = (document.documentElement.lang === navigator.language);

        // this is a special case for netError bug; see https://bugzil.la/444165
        if (document.documentElement.dataset.noCompleteBug) {
            pretranslate.call(navigator.mozL10n);
            return;
        }

        if (isPretranslated) {
            waitFor('interactive', function () {
                window.setTimeout(initResources.bind(navigator.mozL10n));
            });
        } else {
            if (document.readyState === 'complete') {
                window.setTimeout(initResources.bind(navigator.mozL10n));
            } else {
                waitFor('interactive', pretranslate.bind(navigator.mozL10n));
            }
        }

    }

    function pretranslate () {
        if (inlineLocalization.call(this)) {
            waitFor('interactive', function () {
                window.setTimeout(initResources.bind(this));
            }.bind(this));
        } else {
            initResources.call(this);
        }
    }

    function inlineLocalization () {
        var script = document.documentElement
            .querySelector('script[type="application/l10n"]' +
            '[lang="' + navigator.language + '"]');
        if (!script) {
            return false;
        }

        var locale = this.ctx.getLocale(navigator.language);
        // the inline localization is happenning very early, when the ctx is not
        // yet ready and when the resources haven't been downloaded yet;  add the
        // inlined JSON directly to the current locale
        locale.addAST(JSON.parse(script.innerHTML));
        // localize the visible DOM
        var l10n = {
            ctx: locale,
            language: {
                code: locale.id,
                direction: getDirection(locale.id)
            }
        };
        translateDocument.call(l10n);

        // the visible DOM is now pretranslated
        isPretranslated = true;
        return true;
    }

    function initResources () {
        var resLinks = document.head
            .querySelectorAll('link[type="application/l10n"]');
        var iniLinks = [];

        for (var i = 0; i < resLinks.length; i++) {
            var link = resLinks[i];
            var url = link.getAttribute('href');
            var type = url.substr(url.lastIndexOf('.') + 1);
            if (type === 'ini') {
                iniLinks.push(url);
            }
            this.ctx.resLinks.push(url);
        }

        var iniLoads = iniLinks.length;
        if (iniLoads === 0) {
            initLocale.call(this);
            return;
        }

        function onIniLoaded (err) {
            if (err) {
                this.ctx._emitter.emit('error', err);
            }
            if (--iniLoads === 0) {
                initLocale.call(this);
            }
        }

        for (i = 0; i < iniLinks.length; i++) {
            loadINI.call(this, iniLinks[i], onIniLoaded.bind(this));
        }
    }

    function initLocale () {
        this.ctx.requestLocales(navigator.language);
        window.addEventListener('languagechange', function l10n_langchange () {
            navigator.mozL10n.language.code = navigator.language;
        });
    }

    function localizeMutations (mutations) {
        var mutation;

        for (var i = 0; i < mutations.length; i++) {
            mutation = mutations[i];
            if (mutation.type === 'childList') {
                var addedNode;

                for (var j = 0; j < mutation.addedNodes.length; j++) {
                    addedNode = mutation.addedNodes[j];

                    if (addedNode.nodeType !== Node.ELEMENT_NODE) { // eslint-disable-line no-undef
                        continue;
                    }

                    if (addedNode.childElementCount) {
                        translateFragment.call(this, addedNode);
                    } else if (addedNode.hasAttribute('data-l10n-id')) {
                        translateElement.call(this, addedNode);
                    }
                }
            }

            if (mutation.type === 'attributes') {
                translateElement.call(this, mutation.target);
            }
        }
    }

    function onMutations (mutations, self) {
        self.disconnect();
        localizeMutations.call(this, mutations);
        self.observe(document, moConfig);
    }

    function onReady () {
        if (!isPretranslated) {
            translateDocument.call(this);
        }
        isPretranslated = false;

        if (!nodeObserver) {
            nodeObserver = new MutationObserver(onMutations.bind(this)); // eslint-disable-line no-undef
            nodeObserver.observe(document, moConfig);
        }

        fireLocalizedEvent.call(this);
    }

    function fireLocalizedEvent () {
        var event = new CustomEvent('localized', { // eslint-disable-line no-undef
            'bubbles': false,
            'cancelable': false,
            'detail': {
                'language': this.ctx.supportedLocales[0]
            }
        });
        window.dispatchEvent(event);
    }

    function loadINI (url, callback) {
        var ctx = this.ctx;
        io.load(url, function (err, source) {
            var pos = ctx.resLinks.indexOf(url);

            if (err) {
                // remove the ini link from resLinks
                ctx.resLinks.splice(pos, 1);
                return callback(err);
            }

            if (!source) {
                ctx.resLinks.splice(pos, 1);
                return callback(new Error('Empty file: ' + url));
            }

            var patterns = parseINI(source, url).resources.map(function (x) {
                return x.replace('en-US', '{{locale}}');
            });
            ctx.resLinks.splice.apply(ctx.resLinks, [pos, 1].concat(patterns));
            callback();
        });
    }

    function relativePath (baseUrl, url) {
        if (url[0] === '/') {
            return url;
        }

        var dirs = baseUrl.split('/')
            .slice(0, -1)
            .concat(url.split('/'))
            .filter(function (path) {
                return path !== '.';
            });

        return dirs.join('/');
    }

    var iniPatterns = {
        'section': /^\s*\[(.*)\]\s*$/,
        'import': /^\s*@import\s+url\((.*)\)\s*$/i,
        'entry': /[\r\n]+/
    };

    function parseINI (source, iniPath) {
        var entries = source.split(iniPatterns.entry);
        var locales = ['en-US'];
        var genericSection = true;
        var uris = [];
        var match;

        for (var i = 0; i < entries.length; i++) {
            var line = entries[i];
            // we only care about en-US resources
            if (genericSection && iniPatterns['import'].test(line)) {
                match = iniPatterns['import'].exec(line);
                var uri = relativePath(iniPath, match[1]);
                uris.push(uri);
                continue;
            }

            // but we need the list of all locales in the ini, too
            if (iniPatterns.section.test(line)) {
                genericSection = false;
                match = iniPatterns.section.exec(line);
                locales.push(match[1]);
            }
        }
        return {
            locales: locales,
            resources: uris
        };
    }

    function translateDocument () {
        document.documentElement.lang = this.language.code;
        document.documentElement.dir = this.language.direction;
        translateFragment.call(this, document.documentElement);
    }

    function translateFragment (element) {
        if (element.hasAttribute('data-l10n-id')) {
            translateElement.call(this, element);
        }

        var nodes = getTranslatableChildren(element);
        for (var i = 0; i < nodes.length; i++) {
            translateElement.call(this, nodes[i]);
        }
    }

    function setL10nAttributes (element, id, args) {
        element.setAttribute('data-l10n-id', id);
        if (args) {
            element.setAttribute('data-l10n-args', JSON.stringify(args));
        }
    }

    function getL10nAttributes (element) {
        return {
            id: element.getAttribute('data-l10n-id'),
            args: JSON.parse(element.getAttribute('data-l10n-args'))
        };
    }

    function getTranslatableChildren (element) {
        return element ? element.querySelectorAll('*[data-l10n-id]') : [];
    }

    function localizeElement (element, id, args) {
        if (!id) {
            element.removeAttribute('data-l10n-id');
            element.removeAttribute('data-l10n-args');
            setTextContent(element, '');
            return;
        }

        element.setAttribute('data-l10n-id', id);
        if (args && typeof args === 'object') {
            element.setAttribute('data-l10n-args', JSON.stringify(args));
        } else {
            element.removeAttribute('data-l10n-args');
        }
    }

    function translateElement (element) {
        var l10n = getL10nAttributes(element);

        if (!l10n.id) {
            return false;
        }

        var entity = this.ctx.getEntity(l10n.id, l10n.args);

        if (!entity) {
            return false;
        }

        if (typeof entity === 'string') {
            setTextContent(element, entity);
            return true;
        }

        if (entity.value) {
            setTextContent(element, entity.value);
        }

        for (var key in entity.attributes) {
            if (entity.attributes.hasOwnProperty(key)) {
                var attr = entity.attributes[key];
                if (key === 'ariaLabel') {
                    element.setAttribute('aria-label', attr);
                } else if (key === 'innerHTML') {
                    // XXX: to be removed once bug 994357 lands
                    element.innerHTML = attr;
                } else {
                    element.setAttribute(key, attr);
                }
            }
        }

        return true;
    }

    function setTextContent (element, text) {
        // standard case: no element children
        if (!element.firstElementChild) {
            element.textContent = text;
            return;
        }

        // this element has element children: replace the content of the first
        // (non-blank) child textNode and clear other child textNodes
        var found = false;
        var reNotBlank = /\S/;
        for (var child = element.firstChild; child; child = child.nextSibling) {
            if (child.nodeType === Node.TEXT_NODE && // eslint-disable-line no-undef
          reNotBlank.test(child.nodeValue)) {
                if (found) {
                    child.nodeValue = '';
                } else {
                    child.nodeValue = text;
                    found = true;
                }
            }
        }
        // if no (non-empty) textNode is found, insert a textNode before the
        // element's first child.
        if (!found) {
            element.insertBefore(document.createTextNode(text), element.firstChild);
        }
    }

})(this);
