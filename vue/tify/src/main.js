// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import vuetify from './plugins/vuetify.js'

const Vueapp = Vue.extend(App)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vueapp({
  el: '#app',
  router,
  vuetify,
  components: { App },
  template: '<App/>'
})
