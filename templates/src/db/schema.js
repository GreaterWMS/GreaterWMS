import Dexie from 'dexie'

export const db = new Dexie('database')
db.version(1).stores({
  test: 'id, test',
  linechart: 'id, legend, xAxis, serise',
  barchart: 'id, dataset, xAxis, serise ',
  piechart: 'id, data, value, name'
})
db.delete()
db.open()
