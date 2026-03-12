<template>
  <div class="body-app contenu-mobile-app contenu-scroll">
    
    <div v-if="loading" class="loading-screen">
      <div class="spinner"></div>
      <p>Chargement de votre profil...</p>
    </div>

    <template v-else-if="user">
      <header class="header-profil">
        <div class="avatar-conteneur">
          <img :src="`https://ui-avatars.com/api/?name=${user.prenom}+${user.nom}&background=E63946&color=fff&size=128`" 
               alt="Photo de profil" class="photo-profil-grande">
          <div class="badge-edition">✏️</div>
        </div>
        
        <h1 class="nom-utilisateur-profil">{{ user.prenom }} {{ user.nom }}</h1>
        <p class="email-utilisateur">{{ user.email }}</p>

        <div class="infos-academiques">
          <span class="badge-matricule">Matricule : {{ user.matricule }}</span>
          <div class="cursus-tags">
            <span class="tag faculte">{{ user.faculte }}</span>
            <span class="tag departement">{{ user.departement }}</span>
            <span class="tag niveau">{{ user.niveau }}</span>
          </div>
        </div>
      </header>

      <section class="section-stats-profil">
        <div class="carte-stat">
          <span class="chiffre-stat">{{ stats.lus }}</span>
          <span class="label-stat">Rapports lus</span>
        </div>
        <div class="carte-stat">
          <span class="chiffre-stat">{{ stats.en_cours }}</span>
          <span class="label-stat">En cours</span>
        </div>
      </section>

      <section class="section-options">
        <h3 class="sous-titre-gris">Compte & Paramètres</h3>
        <div class="liste-options">
          <div class="item-option">
            <div class="icone-option">📱</div>
            <div class="texte-option">
              <span class="label-option">Téléphone</span>
              <span class="valeur-option">{{ user.telephone }}</span>
            </div>
          </div>

          <button @click="logout" class="item-option deconnexion">
            <div class="icone-option">🚪</div>
            <div class="texte-option">Se déconnecter</div>
          </button>
        </div>
      </section>
    </template>

    <div v-else class="error-screen">
      <p>Oups ! Impossible de charger les données.</p>
      <button @click="fetchUserData" class="btn-retry">Réessayer</button>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const user = ref(null)
const loading = ref(true)
const stats = ref({ lus: 0, en_cours: 0 }) 

// const BASE_URL = 'http://localhost:8000/api'
const BASE_URL = 'http://192.168.189.56:8000/api'


const fetchUserData = async () => {
  loading.value = true
  try {
    const token = localStorage.getItem('access_token')
    if (!token) {
      router.push('/')
      return
    }

    const response = await axios.get(`${BASE_URL}/etudiants/me/`, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    user.value = response.data
  } catch (error) {
    console.error("Erreur Profil:", error)
  } finally {
    loading.value = false
  }
}

const logout = () => {
  if (confirm("Voulez-vous vraiment vous déconnecter ?")) {
    localStorage.clear()
    router.push('/')
  }
}

onMounted(fetchUserData)
</script>

<style scoped>
/* Tes styles CSS ici */
.deconnexion { color: #E63946; cursor: pointer; border: none; background: none; width: 100%; text-align: left; }
</style>