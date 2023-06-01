export function ScanChanged (state, opened) {
  state.scandata = opened
}

export function ScanDataChanged (state, opened) {
  state.datadetail = opened
}

export function ASNDataChanged (state, opened) {
  state.asndata = opened
}

export function DNDataChanged (state, opened) {
  state.dndata = opened
}

export function BinDataChanged (state, opened) {
  state.bindata = opened
}

export function TableDataChanged (state, opened) {
  state.tablelist = opened
}

export function ScanModeChanged (state, opened) {
  state.scanmode = opened
}

export function BarScannedChanged (state, opened) {
  state.bar_scanned = opened
}

export function ApiUrlChanged (state, opened) {
  state.apiurl = opened
}

export function ApiUrlNextChanged (state, opened) {
  state.apiurlnext = opened
}

export function ApiUrlPreviousChanged (state, opened) {
  state.apiurlprevious = opened
}
