import Quasar from 'quasar'

export default async () => {
  const langIso = 'en-us' // ... some logic to determine it (use Cookies Plugin?)

  try {
    await import(
      /* webpackInclude: /(zh-hans|en-us)\.js$/ */
      `quasar/lang/${langIso}`
      )
      .then(lang => {
        Quasar.lang.set(lang.default)
      })
  }
  catch (err) {
    // Requested Quasar Language Pack does not exist,
    // let's not break the app, so catching error
  }
}
