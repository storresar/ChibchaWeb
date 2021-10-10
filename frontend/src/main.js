import { createApp } from 'vue'
import './tailwind.css'
import App from './App.vue'
import { routes } from './routes.js'
import store from './store.js'
import { createRouter, createWebHistory } from 'vue-router'
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

const app = createApp(App)

const router = createRouter({
  history: createWebHistory(),
  routes,
})

app.use(store)
app.use(router)
app.use(VueSweetalert2);
app.mount('#app')
