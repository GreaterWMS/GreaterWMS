import Dexie from 'dexie'

export const db = new Dexie('database')
db.version(1).stores({
  linechart: 'id, legend, xAxis, serise',
  barchart: 'id, dataset, xAxis, serise ',
  piechart: 'id, data, value, name'
})
db.open()
