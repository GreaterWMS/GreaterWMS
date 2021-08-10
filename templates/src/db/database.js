import { db } from './schema'

export class database {
  static getInstance () {
    return new database()
  }

  get () {
    return db
  }
}
