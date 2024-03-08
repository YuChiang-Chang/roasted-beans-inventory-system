import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from './router'
import store from './store'

// createApp(App).use(router).use(store).mount('#app')
axios.defaults.baseURL = 'http://localhost:8000'

const app = createApp(App)
app.use(store)
app.use(router)
app.mount('#app')