<template>
  <div class="contenu-mobile">
    <header class="section-logo">
      <div class="logo-cercle-rouge">🎓</div>
      <h1 class="titre-app-rouge">SOMA</h1>
      <p class="phrase-accroche">Heureux de vous revoir !</p>
    </header>

    <main class="section-formulaire">
      <form @submit.prevent="allerALaccueil" class="formulaire-login">
        
        <div class="groupe-saisie">
          <label class="label-champ">Numéro Matricule</label>
          <input 
            type="text" 
            v-model="matricule" 
            class="champ-texte" 
            placeholder="Ex: 22-FS-0102" 
            required
          >
        </div>
        
        <div class="groupe-saisie">
          <label class="label-champ">Mot de passe</label>
          <input 
            type="password" 
            v-model="password" 
            class="champ-texte" 
            placeholder="••••••••" 
            required
          >
        </div>

        <p v-if="erreur" class="message-erreur">{{ erreur }}</p>

        <div class="options-secondaires">
          <label class="memo-checkbox">
            <input type="checkbox"> <span>Rester connecté</span>
          </label>
          <a href="#" class="lien-oublie-rouge">Oublié ?</a>
        </div>

        <button 
          type="submit" 
          class="bouton-connexion-rouge" 
          :disabled="estEnTrainDeCharger"
        >
          <span v-if="estEnTrainDeCharger">CHARGEMENT...</span>
          <span v-else>SE CONNECTER</span>
        </button>

      </form>
    </main>
    <footer class="section-inscription">
      <p>Nouveau ici ? 
        <router-link to="/inscription" class="lien-inscription-rouge">Créer un compte</router-link>
      </p>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

// --- 1. ÉTATS DU FORMULAIRE ---
const matricule = ref('')
const password = ref('')
const estEnTrainDeCharger = ref(false)
const erreur = ref('')

// --- 2. URL DU SERVEUR ---
const BASE_URL = 'http://localhost:8000/api' // Utilisation du Localhost
// const BASE_URL = 'http://192.168.189.56:8000/api'



// --- 3. MÉTHODE DE CONNEXION ---
const allerALaccueil = async () => {
  estEnTrainDeCharger.value = true
  erreur.value = ''

  try {
    // Django SimpleJWT utilise souvent l'URL /token/ pour la connexion
    const response = await axios.post(`${BASE_URL}/token/`, {
      username: matricule.value, // On envoie le matricule comme 'username'
      password: password.value
    })

    // --- STOCKAGE DES TOKENS (Vu dans ton inspecteur tout à l'heure) ---
    localStorage.setItem('access_token', response.data.access)
    localStorage.setItem('refresh_token', response.data.refresh)
    localStorage.setItem('user_matricule', matricule.value)

    // Redirection vers l'accueil après succès
    alert("Connexion réussie !")
    router.push('/home')

  } catch (err) {
    console.error("Erreur de connexion:", err)
    if (err.response && err.response.status === 401) {
      erreur.value = "Matricule ou mot de passe incorrect."
    } else {
      erreur.value = "Impossible de joindre le serveur Django."
    }
  } finally {
    estEnTrainDeCharger.value = false
  }
}
</script>

<style scoped>
/* Ajoute ce style pour l'erreur */
.message-erreur {
  color: #E63946;
  font-size: 0.85rem;
  text-align: center;
  margin-bottom: 15px;
  font-weight: bold;
}

.bouton-connexion-rouge:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}
</style>