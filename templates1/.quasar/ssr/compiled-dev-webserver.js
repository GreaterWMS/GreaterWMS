var __create = Object.create;
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __getProtoOf = Object.getPrototypeOf;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __esm = (fn, res) => function __init() {
  return fn && (res = (0, fn[__getOwnPropNames(fn)[0]])(fn = 0)), res;
};
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toESM = (mod, isNodeMode, target) => (target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(
  isNodeMode || !mod || !mod.__esModule ? __defProp(target, "default", { value: mod, enumerable: true }) : target,
  mod
));
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// src-ssr/middlewares/render.js
var render_exports = {};
__export(render_exports, {
  default: () => render_default
});
var import_wrappers2, render_default;
var init_render = __esm({
  "src-ssr/middlewares/render.js"() {
    import_wrappers2 = require("quasar/wrappers");
    render_default = (0, import_wrappers2.ssrMiddleware)(({ app, resolve, render, serve }) => {
      app.get(resolve.urlPath("*"), (req, res) => {
        res.setHeader("Content-Type", "text/html");
        render({ req, res }).then((html) => {
          res.send(html);
        }).catch((err) => {
          if (err.url) {
            if (err.code) {
              res.redirect(err.code, err.url);
            } else {
              res.redirect(err.url);
            }
          } else if (err.code === 404) {
            res.status(404).send("404 | Page Not Found");
          } else if (true) {
            serve.error({ err, req, res });
          } else {
            res.status(500).send("500 | Internal Server Error");
          }
        });
      });
    });
  }
});

// .quasar/ssr-dev-webserver.js
var ssr_dev_webserver_exports = {};
__export(ssr_dev_webserver_exports, {
  close: () => close,
  create: () => create,
  injectMiddlewares: () => injectMiddlewares,
  listen: () => listen,
  serveStaticContent: () => serveStaticContent
});
module.exports = __toCommonJS(ssr_dev_webserver_exports);

// src-ssr/server.js
var import_express = __toESM(require("express"));
var import_compression = __toESM(require("compression"));
var import_wrappers = require("quasar/wrappers");
var create = (0, import_wrappers.ssrCreate)(() => {
  const app = (0, import_express.default)();
  app.disable("x-powered-by");
  if (false) {
    app.use((0, import_compression.default)());
  }
  return app;
});
var listen = (0, import_wrappers.ssrListen)(async ({ app, port, isReady }) => {
  await isReady();
  return app.listen(port, () => {
    if (false) {
      console.log("Server listening at port " + port);
    }
  });
});
var close = (0, import_wrappers.ssrClose)(({ listenResult }) => {
  return listenResult.close();
});
var maxAge = true ? 0 : 1e3 * 60 * 60 * 24 * 30;
var serveStaticContent = (0, import_wrappers.ssrServeStaticContent)((path, opts) => {
  return import_express.default.static(path, {
    maxAge,
    ...opts
  });
});
var jsRE = /\.js$/;
var cssRE = /\.css$/;
var woffRE = /\.woff$/;
var woff2RE = /\.woff2$/;
var gifRE = /\.gif$/;
var jpgRE = /\.jpe?g$/;
var pngRE = /\.png$/;
var renderPreloadTag = (0, import_wrappers.ssrRenderPreloadTag)((file) => {
  if (jsRE.test(file) === true) {
    return `<link rel="modulepreload" href="${file}" crossorigin>`;
  }
  if (cssRE.test(file) === true) {
    return `<link rel="stylesheet" href="${file}">`;
  }
  if (woffRE.test(file) === true) {
    return `<link rel="preload" href="${file}" as="font" type="font/woff" crossorigin>`;
  }
  if (woff2RE.test(file) === true) {
    return `<link rel="preload" href="${file}" as="font" type="font/woff2" crossorigin>`;
  }
  if (gifRE.test(file) === true) {
    return `<link rel="preload" href="${file}" as="image" type="image/gif">`;
  }
  if (jpgRE.test(file) === true) {
    return `<link rel="preload" href="${file}" as="image" type="image/jpeg">`;
  }
  if (pngRE.test(file) === true) {
    return `<link rel="preload" href="${file}" as="image" type="image/png">`;
  }
  return "";
});

// .quasar/ssr-middlewares.js
function injectMiddlewares(opts) {
  return Promise.all([
    Promise.resolve().then(() => (init_render(), render_exports))
  ]).then(async (rawMiddlewares) => {
    const middlewares = rawMiddlewares.map((entry) => entry.default);
    for (let i = 0; i < middlewares.length; i++) {
      try {
        await middlewares[i](opts);
      } catch (err) {
        console.error("[Quasar SSR] middleware error:", err);
        return;
      }
    }
  });
}
// Annotate the CommonJS export names for ESM import in node:
0 && (module.exports = {
  close,
  create,
  injectMiddlewares,
  listen,
  serveStaticContent
});
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsiLi4vLi4vc3JjLXNzci9taWRkbGV3YXJlcy9yZW5kZXIuanMiLCAiLi4vc3NyLWRldi13ZWJzZXJ2ZXIuanMiLCAiLi4vLi4vc3JjLXNzci9zZXJ2ZXIuanMiLCAiLi4vc3NyLW1pZGRsZXdhcmVzLmpzIl0sCiAgInNvdXJjZXNDb250ZW50IjogWyJpbXBvcnQgeyBzc3JNaWRkbGV3YXJlIH0gZnJvbSAncXVhc2FyL3dyYXBwZXJzJ1xuXG4vLyBUaGlzIG1pZGRsZXdhcmUgc2hvdWxkIGV4ZWN1dGUgYXMgbGFzdCBvbmVcbi8vIHNpbmNlIGl0IGNhcHR1cmVzIGV2ZXJ5dGhpbmcgYW5kIHRyaWVzIHRvXG4vLyByZW5kZXIgdGhlIHBhZ2Ugd2l0aCBWdWVcblxuZXhwb3J0IGRlZmF1bHQgc3NyTWlkZGxld2FyZSgoeyBhcHAsIHJlc29sdmUsIHJlbmRlciwgc2VydmUgfSkgPT4ge1xuICAvLyB3ZSBjYXB0dXJlIGFueSBvdGhlciBFeHByZXNzIHJvdXRlIGFuZCBoYW5kIGl0XG4gIC8vIG92ZXIgdG8gVnVlIGFuZCBWdWUgUm91dGVyIHRvIHJlbmRlciBvdXIgcGFnZVxuICBhcHAuZ2V0KHJlc29sdmUudXJsUGF0aCgnKicpLCAocmVxLCByZXMpID0+IHtcbiAgICByZXMuc2V0SGVhZGVyKCdDb250ZW50LVR5cGUnLCAndGV4dC9odG1sJylcblxuICAgIHJlbmRlcigvKiB0aGUgc3NyQ29udGV4dDogKi8geyByZXEsIHJlcyB9KVxuICAgICAgLnRoZW4oaHRtbCA9PiB7XG4gICAgICAgIC8vIG5vdyBsZXQncyBzZW5kIHRoZSByZW5kZXJlZCBodG1sIHRvIHRoZSBjbGllbnRcbiAgICAgICAgcmVzLnNlbmQoaHRtbClcbiAgICAgIH0pXG4gICAgICAuY2F0Y2goZXJyID0+IHtcbiAgICAgICAgLy8gb29wcywgd2UgaGFkIGFuIGVycm9yIHdoaWxlIHJlbmRlcmluZyB0aGUgcGFnZVxuXG4gICAgICAgIC8vIHdlIHdlcmUgdG9sZCB0byByZWRpcmVjdCB0byBhbm90aGVyIFVSTFxuICAgICAgICBpZiAoZXJyLnVybCkge1xuICAgICAgICAgIGlmIChlcnIuY29kZSkge1xuICAgICAgICAgICAgcmVzLnJlZGlyZWN0KGVyci5jb2RlLCBlcnIudXJsKVxuICAgICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgICByZXMucmVkaXJlY3QoZXJyLnVybClcbiAgICAgICAgICB9XG4gICAgICAgIH0gZWxzZSBpZiAoZXJyLmNvZGUgPT09IDQwNCkge1xuICAgICAgICAgIC8vIGhtbSwgVnVlIFJvdXRlciBjb3VsZCBub3QgZmluZCB0aGUgcmVxdWVzdGVkIHJvdXRlXG5cbiAgICAgICAgICAvLyBTaG91bGQgcmVhY2ggaGVyZSBvbmx5IGlmIG5vIFwiY2F0Y2gtYWxsXCIgcm91dGVcbiAgICAgICAgICAvLyBpcyBkZWZpbmVkIGluIC9zcmMvcm91dGVzXG4gICAgICAgICAgcmVzLnN0YXR1cyg0MDQpLnNlbmQoJzQwNCB8IFBhZ2UgTm90IEZvdW5kJylcbiAgICAgICAgfSBlbHNlIGlmIChwcm9jZXNzLmVudi5ERVYpIHtcbiAgICAgICAgICAvLyB3ZWxsLCB3ZSB0cmVhdCBhbnkgb3RoZXIgY29kZSBhcyBlcnJvcjtcbiAgICAgICAgICAvLyBpZiB3ZSdyZSBpbiBkZXYgbW9kZSwgdGhlbiB3ZSBjYW4gdXNlIFF1YXNhciBDTElcbiAgICAgICAgICAvLyB0byBkaXNwbGF5IGEgbmljZSBlcnJvciBwYWdlIHRoYXQgY29udGFpbnMgdGhlIHN0YWNrXG4gICAgICAgICAgLy8gYW5kIG90aGVyIHVzZWZ1bCBpbmZvcm1hdGlvblxuXG4gICAgICAgICAgLy8gc2VydmUuZXJyb3IgaXMgYXZhaWxhYmxlIG9uIGRldiBvbmx5XG4gICAgICAgICAgc2VydmUuZXJyb3IoeyBlcnIsIHJlcSwgcmVzIH0pXG4gICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgLy8gd2UncmUgaW4gcHJvZHVjdGlvbiwgc28gd2Ugc2hvdWxkIGhhdmUgYW5vdGhlciBtZXRob2RcbiAgICAgICAgICAvLyB0byBkaXNwbGF5IHNvbWV0aGluZyB0byB0aGUgY2xpZW50IHdoZW4gd2UgZW5jb3VudGVyIGFuIGVycm9yXG4gICAgICAgICAgLy8gKGZvciBzZWN1cml0eSByZWFzb25zLCBpdCdzIG5vdCBvayB0byBkaXNwbGF5IHRoZSBzYW1lIHdlYWx0aFxuICAgICAgICAgIC8vIG9mIGluZm9ybWF0aW9uIGFzIHdlIGRvIGluIGRldmVsb3BtZW50KVxuXG4gICAgICAgICAgLy8gUmVuZGVyIEVycm9yIFBhZ2Ugb24gcHJvZHVjdGlvbiBvclxuICAgICAgICAgIC8vIGNyZWF0ZSBhIHJvdXRlICgvc3JjL3JvdXRlcykgZm9yIGFuIGVycm9yIHBhZ2UgYW5kIHJlZGlyZWN0IHRvIGl0XG4gICAgICAgICAgcmVzLnN0YXR1cyg1MDApLnNlbmQoJzUwMCB8IEludGVybmFsIFNlcnZlciBFcnJvcicpXG4gICAgICAgICAgLy8gY29uc29sZS5lcnJvcihlcnIuc3RhY2spXG4gICAgICAgIH1cbiAgICAgIH0pXG4gIH0pXG59KVxuIiwgIi8qIGVzbGludC1kaXNhYmxlICovXG4vKipcbiAqIFRISVMgRklMRSBJUyBHRU5FUkFURUQgQVVUT01BVElDQUxMWS5cbiAqIERPIE5PVCBFRElULlxuICoqL1xuXG5pbXBvcnQgeyBjcmVhdGUsIGxpc3RlbiwgY2xvc2UsIHNlcnZlU3RhdGljQ29udGVudCB9IGZyb20gJy4uL3NyYy1zc3Ivc2VydmVyJ1xuaW1wb3J0IGluamVjdE1pZGRsZXdhcmVzIGZyb20gJy4vc3NyLW1pZGRsZXdhcmVzJ1xuXG5leHBvcnQge1xuICBjcmVhdGUsXG4gIGxpc3RlbixcbiAgY2xvc2UsXG4gIHNlcnZlU3RhdGljQ29udGVudCxcbiAgaW5qZWN0TWlkZGxld2FyZXNcbn1cbiIsICIvKipcbiAqIE1vcmUgaW5mbyBhYm91dCB0aGlzIGZpbGU6XG4gKiBodHRwczovL3YyLnF1YXNhci5kZXYvcXVhc2FyLWNsaS12aXRlL2RldmVsb3Bpbmctc3NyL3Nzci13ZWJzZXJ2ZXJcbiAqXG4gKiBSdW5zIGluIE5vZGUgY29udGV4dC5cbiAqL1xuXG4vKipcbiAqIE1ha2Ugc3VyZSB0byB5YXJuIGFkZCAvIG5wbSBpbnN0YWxsIChpbiB5b3VyIHByb2plY3Qgcm9vdClcbiAqIGFueXRoaW5nIHlvdSBpbXBvcnQgaGVyZSAoZXhjZXB0IGZvciBleHByZXNzIGFuZCBjb21wcmVzc2lvbikuXG4gKi9cbmltcG9ydCBleHByZXNzIGZyb20gJ2V4cHJlc3MnXG5pbXBvcnQgY29tcHJlc3Npb24gZnJvbSAnY29tcHJlc3Npb24nXG5pbXBvcnQge1xuICBzc3JDbG9zZSxcbiAgc3NyQ3JlYXRlLFxuICBzc3JMaXN0ZW4sXG4gIHNzclJlbmRlclByZWxvYWRUYWcsXG4gIHNzclNlcnZlU3RhdGljQ29udGVudFxufSBmcm9tICdxdWFzYXIvd3JhcHBlcnMnXG5cbi8qKlxuICogQ3JlYXRlIHlvdXIgd2Vic2VydmVyIGFuZCByZXR1cm4gaXRzIGluc3RhbmNlLlxuICogSWYgbmVlZGVkLCBwcmVwYXJlIHlvdXIgd2Vic2VydmVyIHRvIHJlY2VpdmVcbiAqIGNvbm5lY3QtbGlrZSBtaWRkbGV3YXJlcy5cbiAqXG4gKiBTaG91bGQgTk9UIGJlIGFzeW5jIVxuICovXG5leHBvcnQgY29uc3QgY3JlYXRlID0gc3NyQ3JlYXRlKCgvKiB7IC4uLiB9ICovKSA9PiB7XG4gIGNvbnN0IGFwcCA9IGV4cHJlc3MoKVxuXG4gIC8vIGF0dGFja2VycyBjYW4gdXNlIHRoaXMgaGVhZGVyIHRvIGRldGVjdCBhcHBzIHJ1bm5pbmcgRXhwcmVzc1xuICAvLyBhbmQgdGhlbiBsYXVuY2ggc3BlY2lmaWNhbGx5LXRhcmdldGVkIGF0dGFja3NcbiAgYXBwLmRpc2FibGUoJ3gtcG93ZXJlZC1ieScpXG5cbiAgLy8gcGxhY2UgaGVyZSBhbnkgbWlkZGxld2FyZXMgdGhhdFxuICAvLyBhYnNvbHV0ZWx5IG5lZWQgdG8gcnVuIGJlZm9yZSBhbnl0aGluZyBlbHNlXG4gIGlmIChwcm9jZXNzLmVudi5QUk9EKSB7XG4gICAgYXBwLnVzZShjb21wcmVzc2lvbigpKVxuICB9XG5cbiAgcmV0dXJuIGFwcFxufSlcblxuLyoqXG4gKiBZb3UgbmVlZCB0byBtYWtlIHRoZSBzZXJ2ZXIgbGlzdGVuIHRvIHRoZSBpbmRpY2F0ZWQgcG9ydFxuICogYW5kIHJldHVybiB0aGUgbGlzdGVuaW5nIGluc3RhbmNlIG9yIHdoYXRldmVyIHlvdSBuZWVkIHRvXG4gKiBjbG9zZSB0aGUgc2VydmVyIHdpdGguXG4gKlxuICogVGhlIFwibGlzdGVuUmVzdWx0XCIgcGFyYW0gZm9yIHRoZSBcImNsb3NlKClcIiBkZWZpbml0aW9uIGJlbG93XG4gKiBpcyB3aGF0IHlvdSByZXR1cm4gaGVyZS5cbiAqXG4gKiBGb3IgcHJvZHVjdGlvbiwgeW91IGNhbiBpbnN0ZWFkIGV4cG9ydCB5b3VyXG4gKiBoYW5kbGVyIGZvciBzZXJ2ZXJsZXNzIHVzZSBvciB3aGF0ZXZlciBlbHNlIGZpdHMgeW91ciBuZWVkcy5cbiAqL1xuZXhwb3J0IGNvbnN0IGxpc3RlbiA9IHNzckxpc3Rlbihhc3luYyAoeyBhcHAsIHBvcnQsIGlzUmVhZHkgfSkgPT4ge1xuICBhd2FpdCBpc1JlYWR5KClcbiAgcmV0dXJuIGFwcC5saXN0ZW4ocG9ydCwgKCkgPT4ge1xuICAgIGlmIChwcm9jZXNzLmVudi5QUk9EKSB7XG4gICAgICBjb25zb2xlLmxvZygnU2VydmVyIGxpc3RlbmluZyBhdCBwb3J0ICcgKyBwb3J0KVxuICAgIH1cbiAgfSlcbn0pXG5cbi8qKlxuICogU2hvdWxkIGNsb3NlIHRoZSBzZXJ2ZXIgYW5kIGZyZWUgdXAgYW55IHJlc291cmNlcy5cbiAqIFdpbGwgYmUgdXNlZCBvbiBkZXZlbG9wbWVudCBvbmx5IHdoZW4gdGhlIHNlcnZlciBuZWVkc1xuICogdG8gYmUgcmVib290ZWQuXG4gKlxuICogU2hvdWxkIHlvdSBuZWVkIHRoZSByZXN1bHQgb2YgdGhlIFwibGlzdGVuKClcIiBjYWxsIGFib3ZlLFxuICogeW91IGNhbiB1c2UgdGhlIFwibGlzdGVuUmVzdWx0XCIgcGFyYW0uXG4gKlxuICogQ2FuIGJlIGFzeW5jLlxuICovXG5leHBvcnQgY29uc3QgY2xvc2UgPSBzc3JDbG9zZSgoeyBsaXN0ZW5SZXN1bHQgfSkgPT4ge1xuICByZXR1cm4gbGlzdGVuUmVzdWx0LmNsb3NlKClcbn0pXG5cbmNvbnN0IG1heEFnZSA9IHByb2Nlc3MuZW52LkRFVlxuICA/IDBcbiAgOiAxMDAwICogNjAgKiA2MCAqIDI0ICogMzBcblxuLyoqXG4gKiBTaG91bGQgcmV0dXJuIG1pZGRsZXdhcmUgdGhhdCBzZXJ2ZXMgdGhlIGluZGljYXRlZCBwYXRoXG4gKiB3aXRoIHN0YXRpYyBjb250ZW50LlxuICovXG5leHBvcnQgY29uc3Qgc2VydmVTdGF0aWNDb250ZW50ID0gc3NyU2VydmVTdGF0aWNDb250ZW50KChwYXRoLCBvcHRzKSA9PiB7XG4gIHJldHVybiBleHByZXNzLnN0YXRpYyhwYXRoLCB7XG4gICAgbWF4QWdlLFxuICAgIC4uLm9wdHNcbiAgfSlcbn0pXG5cbmNvbnN0IGpzUkUgPSAvXFwuanMkL1xuY29uc3QgY3NzUkUgPSAvXFwuY3NzJC9cbmNvbnN0IHdvZmZSRSA9IC9cXC53b2ZmJC9cbmNvbnN0IHdvZmYyUkUgPSAvXFwud29mZjIkL1xuY29uc3QgZ2lmUkUgPSAvXFwuZ2lmJC9cbmNvbnN0IGpwZ1JFID0gL1xcLmpwZT9nJC9cbmNvbnN0IHBuZ1JFID0gL1xcLnBuZyQvXG5cbi8qKlxuICogU2hvdWxkIHJldHVybiBhIFN0cmluZyB3aXRoIEhUTUwgb3V0cHV0XG4gKiAoaWYgYW55KSBmb3IgcHJlbG9hZGluZyBpbmRpY2F0ZWQgZmlsZVxuICovXG5leHBvcnQgY29uc3QgcmVuZGVyUHJlbG9hZFRhZyA9IHNzclJlbmRlclByZWxvYWRUYWcoKGZpbGUpID0+IHtcbiAgaWYgKGpzUkUudGVzdChmaWxlKSA9PT0gdHJ1ZSkge1xuICAgIHJldHVybiBgPGxpbmsgcmVsPVwibW9kdWxlcHJlbG9hZFwiIGhyZWY9XCIke2ZpbGV9XCIgY3Jvc3NvcmlnaW4+YFxuICB9XG5cbiAgaWYgKGNzc1JFLnRlc3QoZmlsZSkgPT09IHRydWUpIHtcbiAgICByZXR1cm4gYDxsaW5rIHJlbD1cInN0eWxlc2hlZXRcIiBocmVmPVwiJHtmaWxlfVwiPmBcbiAgfVxuXG4gIGlmICh3b2ZmUkUudGVzdChmaWxlKSA9PT0gdHJ1ZSkge1xuICAgIHJldHVybiBgPGxpbmsgcmVsPVwicHJlbG9hZFwiIGhyZWY9XCIke2ZpbGV9XCIgYXM9XCJmb250XCIgdHlwZT1cImZvbnQvd29mZlwiIGNyb3Nzb3JpZ2luPmBcbiAgfVxuXG4gIGlmICh3b2ZmMlJFLnRlc3QoZmlsZSkgPT09IHRydWUpIHtcbiAgICByZXR1cm4gYDxsaW5rIHJlbD1cInByZWxvYWRcIiBocmVmPVwiJHtmaWxlfVwiIGFzPVwiZm9udFwiIHR5cGU9XCJmb250L3dvZmYyXCIgY3Jvc3NvcmlnaW4+YFxuICB9XG5cbiAgaWYgKGdpZlJFLnRlc3QoZmlsZSkgPT09IHRydWUpIHtcbiAgICByZXR1cm4gYDxsaW5rIHJlbD1cInByZWxvYWRcIiBocmVmPVwiJHtmaWxlfVwiIGFzPVwiaW1hZ2VcIiB0eXBlPVwiaW1hZ2UvZ2lmXCI+YFxuICB9XG5cbiAgaWYgKGpwZ1JFLnRlc3QoZmlsZSkgPT09IHRydWUpIHtcbiAgICByZXR1cm4gYDxsaW5rIHJlbD1cInByZWxvYWRcIiBocmVmPVwiJHtmaWxlfVwiIGFzPVwiaW1hZ2VcIiB0eXBlPVwiaW1hZ2UvanBlZ1wiPmBcbiAgfVxuXG4gIGlmIChwbmdSRS50ZXN0KGZpbGUpID09PSB0cnVlKSB7XG4gICAgcmV0dXJuIGA8bGluayByZWw9XCJwcmVsb2FkXCIgaHJlZj1cIiR7ZmlsZX1cIiBhcz1cImltYWdlXCIgdHlwZT1cImltYWdlL3BuZ1wiPmBcbiAgfVxuXG4gIHJldHVybiAnJ1xufSlcbiIsICIvKiBlc2xpbnQtZGlzYWJsZSAqL1xuLyoqXG4gKiBUSElTIEZJTEUgSVMgR0VORVJBVEVEIEFVVE9NQVRJQ0FMTFkuXG4gKiBETyBOT1QgRURJVC5cbiAqKi9cblxuZXhwb3J0IGRlZmF1bHQgZnVuY3Rpb24gaW5qZWN0TWlkZGxld2FyZXMgKG9wdHMpIHtcbiAgcmV0dXJuIFByb21pc2UuYWxsKFtcbiAgICBcbiAgICBpbXBvcnQoJ3NyYy1zc3IvbWlkZGxld2FyZXMvcmVuZGVyJylcbiAgICBcbiAgXSkudGhlbihhc3luYyByYXdNaWRkbGV3YXJlcyA9PiB7XG4gICAgY29uc3QgbWlkZGxld2FyZXMgPSByYXdNaWRkbGV3YXJlc1xuICAgICAgLm1hcChlbnRyeSA9PiBlbnRyeS5kZWZhdWx0KVxuXG4gICAgZm9yIChsZXQgaSA9IDA7IGkgPCBtaWRkbGV3YXJlcy5sZW5ndGg7IGkrKykge1xuICAgICAgdHJ5IHtcbiAgICAgICAgYXdhaXQgbWlkZGxld2FyZXNbaV0ob3B0cylcbiAgICAgIH1cbiAgICAgIGNhdGNoIChlcnIpIHtcbiAgICAgICAgY29uc29sZS5lcnJvcignW1F1YXNhciBTU1JdIG1pZGRsZXdhcmUgZXJyb3I6JywgZXJyKVxuICAgICAgICByZXR1cm5cbiAgICAgIH1cbiAgICB9XG4gIH0pXG59XG4iXSwKICAibWFwcGluZ3MiOiAiOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQSxJQUFBQSxrQkFNTztBQU5QO0FBQUE7QUFBQSxJQUFBQSxtQkFBOEI7QUFNOUIsSUFBTyxxQkFBUSxnQ0FBYyxDQUFDLEVBQUUsS0FBSyxTQUFTLFFBQVEsTUFBTSxNQUFNO0FBR2hFLFVBQUksSUFBSSxRQUFRLFFBQVEsR0FBRyxHQUFHLENBQUMsS0FBSyxRQUFRO0FBQzFDLFlBQUksVUFBVSxnQkFBZ0IsV0FBVztBQUV6QyxlQUE2QixFQUFFLEtBQUssSUFBSSxDQUFDLEVBQ3RDLEtBQUssVUFBUTtBQUVaLGNBQUksS0FBSyxJQUFJO0FBQUEsUUFDZixDQUFDLEVBQ0EsTUFBTSxTQUFPO0FBSVosY0FBSSxJQUFJLEtBQUs7QUFDWCxnQkFBSSxJQUFJLE1BQU07QUFDWixrQkFBSSxTQUFTLElBQUksTUFBTSxJQUFJLEdBQUc7QUFBQSxZQUNoQyxPQUFPO0FBQ0ws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
