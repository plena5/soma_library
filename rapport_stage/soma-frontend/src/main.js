import { createApp } from 'vue'
import App from './App.vue'
import router from './router' // Importe la configuration depuis src/router/index.js

// On crée l'application, on lui injecte le router, et on l'affiche dans la div #app
createApp(App)
  .use(router)
  .mount('#app')