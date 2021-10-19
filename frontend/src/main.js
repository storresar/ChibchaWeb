import { createApp } from 'vue/dist/vue.esm-bundler';
import './tailwind.css'
import App from './App.vue'
import router from './routes.js'
import store from './store.js'
import VueSweetalert2 from 'vue-sweetalert2'
import 'sweetalert2/dist/sweetalert2.min.css'
import Popper from "vue3-popper";


const app = createApp(App)

app.use(store)
app.use(router)
app.use(VueSweetalert2);
app.mount('#app')

app.component("Popper", Popper);