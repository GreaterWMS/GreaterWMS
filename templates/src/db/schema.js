import Dexie from 'dexie'

export const db = new Dexie('database')
db.version(1).stores({
  test: 'id, test'
})
db.delete()
db.open()
