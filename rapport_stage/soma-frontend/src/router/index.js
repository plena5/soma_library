import { createRouter, createWebHistory } from 'vue-router'

// 1. On importe la page de départ normalement
import CommenceView from '../views/CommenceView.vue'


const routes = [
  {
    path: '/',
    name: 'start', // Utilisé dans App.vue pour masquer le menu
    component: CommenceView
  },
  {
    path: '/inscription',
    name: 'inscription', // Utilisé dans App.vue pour masquer le menu
    component: () => import('../views/InscriptionView.vue')
  },
  {
    path: '/connexion',
    name: 'connexion', // Utilisé dans App.vue pour masquer le menu
    component: () => import('../views/ConnexionView.vue')
  },
  {
    path: '/home',
    name: 'home',
    component: () => import('../views/AccueilView.vue')
  },
  {
    path: '/catalogue',
    name: 'catalogue',
    component: () => import('../views/CatalogueView.vue')
  },
  {
    path: '/ma-bibliotheque',
    name: 'ma-bibliotheque', // J'ai renommé pour correspondre à l'URL
    component: () => import('../views/Ma_bibliothequeView.vue')
  },
  {
    path: '/profil',
    name: 'profil',
    component: () => import('../views/ProfileView.vue')
  },

  {
  path: '/lecture/:id',  // Le :id est dynamique
  name: 'lecture',
  component: () => import('../views/LectureView.vue')
}
]

const router = createRouter({
  // Utilise l'historique du navigateur
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router