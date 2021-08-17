const protocol = location.protocol;

const host = window.location.host;

const baseurl = `${protocol}//${host}/`,
  wsurl = `${protocol === "https" ? "wss:" : "ws:"}//${host}/`;

window.g = { BaseUrl: baseurl, WsUrl: wsurl };
