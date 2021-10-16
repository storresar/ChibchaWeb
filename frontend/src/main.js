import { createApp } from 'vue'
import './tailwind.css'
import App from './App.vue'
import router from './routes.js'
import store from './store.js'
import VueSweetalert2 from 'vue-sweetalert2'
import 'sweetalert2/dist/sweetalert2.min.css'


console.log(import.meta.env);

const app = createApp(App)

app.use(store)
app.use(router)
app.use(VueSweetalert2);
app.mount('#app')
