import Quasar from 'quasar'

export default async () => {
  const langIso = 'en-US' // ... some logic to determine it (use Cookies Plugin?)

  try {
    await import(
      /* webpackInclude: /(zh-hans|en-US)\.js$/ */
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
