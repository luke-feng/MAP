import Vue from 'vue'
import App from './App.vue'
import VueBlu from 'vue-blu'
import './registerServiceWorker'
import router from './router'
import store from './store'
import Button from 'ant-design-vue/lib/button'
import 'ant-design-vue/dist/antd.css'
import DropdownMenu from '@innologica/vue-dropdown-menu'
import VueSidebarMenu from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'
import vueResource from 'vue-resource'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import 'vue-blu/dist/css/vue-blu.min.css'
import qs from 'qs'
import axios from 'axios'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/en'
Vue.use(ElementUI, { locale })
Vue.use(vueResource)
Vue.use(Button)
Vue.use(VueMaterial)
Vue.use(VueBlu)
Vue.use(DropdownMenu)
Vue.use(VueSidebarMenu)
Vue.use(VueMaterial)
Vue.config.productionTip = false
Vue.prototype.$axios = axios
Vue.prototype.$qs = qs

new Vue({
  router,
  store,
  axios,
  render: h => h(App)
}).$mount('#app')
