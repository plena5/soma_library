<template>
  <div class="contenu-mobile">
    <header class="section-logo">
      <div class="logo-cercle-rouge">🎓</div>
      <h1 class="titre-app-rouge">SOMA</h1>
      <p class="phrase-accroche">Rejoignez la communauté SOMA</p>
    </header>

    <main class="section-formulaire">
      <form @submit.prevent="creerCompte" class="formulaire-login">
        
        <div class="groupe-saisie">
          <label class="label-champ">Nom</label>
          <input type="text" v-model="form.nom" class="champ-texte" placeholder="Votre nom" required>
        </div>

        <div class="groupe-saisie">
          <label class="label-champ">Prénom</label>
          <input type="text" v-model="form.prenom" class="champ-texte" placeholder="Votre prénom" required>
        </div>

        <div class="groupe-saisie">
          <label class="label-champ">Email</label>
          <input type="email" v-model="form.email" class="champ-texte" placeholder="exemple@univ.edu" required>
        </div>

        <div class="groupe-saisie">
          <label class="label-champ">Téléphone</label>
          <input type="tel" v-model="form.telephone" class="champ-texte" placeholder="+257.." required>
        </div>

        <div class="groupe-saisie">
          <label class="label-champ">Numéro Matricule</label>
          <input type="text" v-model="form.matricule" class="champ-texte" placeholder="Ex: 22234/23" required>
        </div>

        <div class="groupe-saisie">
          <label class="label-champ">Faculté</label>
          <select v-model="form.faculte" @change="filtrerDepartements" class="champ-texte" required>
            <option value="" disabled>Choisir une faculté</option>
            <option v-for="f in facultes" :key="f.id" :value="f.id">{{ f.nom }}</option>
          </select>
        </div>
        <div class="groupe-saisie">
  <label>Département</label>
  <select 
    v-model="form.departement" 
    class="champ-texte"
    :disabled="departementsFiltrés.length === 0"
  >
    <option value="">
      {{ departementsFiltrés.length === 0 ? 'Choisissez d\'abord une faculté' : 'Sélectionnez un département' }}
    </option>
    <option v-for="d in departementsFiltrés" :key="d.id" :value="d.id">
      {{ d.nom }}
    </option>
  </select>
</div>

        

        <div class="groupe-saisie">
          <label class="label-champ">Niveau actuel</label>
          <select v-model="form.niveau" class="champ-texte" required>
            <option value="" disabled>Votre niveau (L1, M1...)</option>
            <option v-for="n in niveaux" :key="n.id" :value="n.id">{{ n.nom }}</option>
          </select>
        </div>

        <div class="groupe-saisie">
          <label class="label-champ">Mot de passe</label>
          <input type="password" v-model="form.password" class="champ-texte" placeholder="••••••••" required>
        </div>

        <p v-if="erreur" class="erreur-msg">{{ erreur }}</p>

        <button type="submit" class="bouton-connexion-rouge" :disabled="chargement">
          <span v-if="chargement">CRÉATION EN COURS...</span>
          <span v-else>CRÉER MON COMPTE</span>
        </button>
      </form>
    </main>

    <footer class="section-inscription">
      <p>Déjà inscrit ? 
        <router-link to="/connexion" class="lien-inscription-rouge">Se connecter</router-link>
      </p>
    </footer>
  </div>
</template>




<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const BASE_URL = 'http://localhost:8000/api'
// const BASE_URL = 'http://192.168.189.56:8000/api'


const savedForm = localStorage.getItem('soma_brouillon')
const form = ref(savedForm ? JSON.parse(savedForm) : {
  nom: '',
  prenom: '',
  email: '',
  telephone: '',
  matricule: '',
  faculte: '',
  departement: '',
  niveau: '',
  password: ''
})

// --- 2. ÉTATS DE L'APPLICATION ---
const facultes = ref([])
const tousLesDepartements = ref([])
const departementsFiltrés = ref([])
const niveaux = ref([])
const chargement = ref(false)
const erreur = ref('')
const estOnline = ref(navigator.onLine)

// --- 3. LES WATCHERS (Modèle Point 7) ---

// Sauvegarde automatique du brouillon dans le Local Storage
watch(form, (nouveauForm) => {
  localStorage.setItem('soma_brouillon', JSON.stringify(nouveauForm))
}, { deep: true })

// Filtrage automatique : on a enlevé "nouvelleFac" pour éviter l'erreur Webpack
watch(() => form.value.faculte, () => {
  filtrerDepartements()
})

// --- 4. MÉTHODES ---

const filtrerDepartements = () => {
  if (!form.value.faculte) {
    departementsFiltrés.value = []
    return
  }

  // Filtrage robuste : conversion en String pour comparer IDs numériques et texte
  departementsFiltrés.value = tousLesDepartements.value.filter(d => {
    const idFacInDep = d.faculte?.id || d.faculte
    return String(idFacInDep) === String(form.value.faculte)
  })
}

const chargerListes = async () => {
  // A. Récupération depuis le Local Storage (Mode Offline-First)
  const cachedFacs = localStorage.getItem('cache_facultes')
  const cachedDeps = localStorage.getItem('cache_departements')
  const cachedNivs = localStorage.getItem('cache_niveaux')

  if (cachedFacs) facultes.value = JSON.parse(cachedFacs)
  if (cachedDeps) tousLesDepartements.value = JSON.parse(cachedDeps)
  if (cachedNivs) niveaux.value = JSON.parse(cachedNivs)
  
  if (form.value.faculte) filtrerDepartements()

  // B. Mise à jour depuis le serveur Django
  try {
    const [resFac, resDep, resNiv] = await Promise.all([
      axios.get(`${BASE_URL}/facultes/`),
      axios.get(`${BASE_URL}/departements/`),
      axios.get(`${BASE_URL}/niveaux/`)
    ])
    
    facultes.value = resFac.data
    tousLesDepartements.value = resDep.data
    niveaux.value = resNiv.data

    // Sauvegarde des listes pour le travail hors-ligne
    localStorage.setItem('cache_facultes', JSON.stringify(resFac.data))
    localStorage.setItem('cache_departements', JSON.stringify(resDep.data))
    localStorage.setItem('cache_niveaux', JSON.stringify(resNiv.data))
    
    if (form.value.faculte) filtrerDepartements()
    
  } catch (e) {
    console.warn("Mode hors-ligne : Utilisation des données locales.")
    if (!facultes.value.length) {
      erreur.value = "Impossible de charger les listes du serveur."
    }
  }
}

const creerCompte = async () => {
  if (!navigator.onLine) {
    alert("⚠️ Pas d'internet. Les données sont conservées localement.")
    return
  }

  chargement.value = true
  erreur.value = ''
  try {
    await axios.post(`${BASE_URL}/etudiants/inscription/`, form.value)
    
    // Nettoyage après succès (Modèle Point 5)
    localStorage.removeItem('brouillon')
    
    alert("Compte créé avec succès !")
    router.push('/connexion')
  } catch (e) {
    erreur.value = e.response?.data?.error || "Erreur lors de l'inscription."
  } finally {
    chargement.value = false
  }
}

onMounted(() => {
  chargerListes()
  window.addEventListener('online', () => {
    estOnline.value = true
    chargerListes()
  })
  window.addEventListener('offline', () => estOnline.value = false)
})
</script>

<style scoped>
.erreur-msg {
  color: #E63946;
  text-align: center;
  font-size: 0.9rem;
  margin-bottom: 10px;
}
.bouton-connexion-rouge:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}
</style>