<template>
  <div class="contenu-mobile-app contenu-scroll">
    <header class="header-accueil">
      <div class="infos-utilisateur">
        <span class="salutation">Ma Bibliothèque</span>
        <h1 class="titre-section">SOMA Catalogue</h1>
        <div class="phrase-inspiration">
          <p>"Le savoir est la seule richesse que l'on peut diviser sans la diminuer."</p>
        </div>
      </div>
      <div class="logo-mini-rouge">🔍</div>
    </header>
<section class="section-reprise" v-if="dernierDocument">
  <div class="carte-bleue-reprise">
    <div class="contenu-reprise">
      <span class="badge-status">EN COURS</span>
      
      <h2 class="titre-livre-reprise">{{ dernierDocument.document_titre }}</h2>
      <p class="auteur-livre-reprise">Par {{ dernierDocument.auteur_nom }}</p>


      
<!--       
      <div class="conteneur-barre-progression">
        <div class="barre-niveau-lecture" :style="{ width: progression + '%' }"></div>
      </div>
      <span class="info-pourcentage">{{ progression }}% terminé</span>-->
    </div>

    <div class="contenu-reprise">
  <div class="conteneur-barre-progression">
    <div 
      class="barre-niveau-lecture" 
      :style="{ width: progressionDynamique + '%' }"
    ></div>
  </div>

  <span class="info-pourcentage">{{ progressionDynamique }}% terminé</span>
</div>

    <button @click="$router.push(`/lecture/${dernierDocument.document}`)" class="btn-lire">
      LIRE
    </button>
  </div>
</section>

<section v-else class="section-reprise-vide">
  <p>Aucune lecture en cours. Parcourez le catalogue !</p>
</section>

<section class="section-bibliotheque">
  <h2>Tous les documents</h2>
  
  <div class="grille-documents">
    <div v-for="doc in documents" :key="doc.id" class="carte-document">
      <div class="image-placeholder">📄</div>
      
      <div class="infos">
        <h3>{{ doc.exercice_traite }}</h3>
        <p class="institution">{{ doc.institution }}</p>
        
        <span class="badge-pages">{{ doc.nombre_pages_total }} pages</span>
      </div>

      <button @click="$router.push(`/lecture/${doc.id}`)" class="btn-ouvrir">
        OUVRIR LE DOCUMENT
      </button>
    </div>
  </div>

  <p v-if="documents.length === 0" class="message-vide">
    La bibliothèque est vide pour le moment.
  </p>
</section>
    
    <!-- <section class="section-reprise">
      <div class="carte-bleue-reprise">
        <div class="contenu-reprise">
          <span class="badge-status">EN COURS</span>
          <h2 class="titre-livre-reprise">Audit de Sécurité IT</h2>
          <p class="auteur-livre-reprise">Par Sarah Mutombo</p>
          
          <div class="conteneur-barre-progression">
            <div class="barre-niveau-lecture" :style="{ width: progression + '%' }"></div>
          </div>
          <span class="info-pourcentage">{{ progression }}% terminé</span>
        </div>
        
   

<button @click="$router.push(`/lecture/${doc.id}`)" class="btn-lire">
          LIRE
        </button>
    
      </div>

      
    </section> -->

    <section class="section-galerie">
      <div class="zone-recherche-filtre">
        <div class="barre-recherche-conteneur">
          <span class="icone-loupe">🔍</span>
          <input 
            type="text" 
            class="input-recherche" 
            placeholder="Rechercher un rapport..."
            v-model="recherche"
          >
        </div>
        <button class="bouton-filtrer-icone">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="21" x2="4" y2="14"></line><line x1="4" y1="10" x2="4" y2="3"></line><line x1="12" y1="21" x2="12" y2="12"></line><line x1="12" y1="8" x2="12" y2="3"></line><line x1="20" y1="21" x2="20" y2="16"></line><line x1="20" y1="12" x2="20" y2="3"></line><line x1="2" y1="14" x2="6" y2="14"></line><line x1="10" y1="8" x2="14" y2="8"></line><line x1="18" y1="16" x2="22" y2="16"></line></svg>
        </button>
      </div>

      <div class="flex-titre">
        <h2 class="sous-titre">Découvrir d'autres travaux</h2>
      </div>

      <div class="scroll-couvertures">
        <div class="carte-rapport">
          <div class="couverture-preview stage">
            <img src="https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=300" class="image-fond">
            <span class="type-badge badge-stage">STAGE</span>
          </div>
          <div class="infos-carte">
            <h4 class="sujet-traite">Marketing Digital</h4>
            <p class="auteur">Marc Kabeya</p>
          </div>
        </div>

        <div class="carte-rapport">
          <div class="couverture-preview memoire">
            <img src="https://images.unsplash.com/photo-1454165833767-027508496b41?auto=format&fit=crop&w=300" class="image-fond">
            <span class="type-badge badge-memoire">MÉMOIRE</span>
          </div>
          <div class="infos-carte">
            <h4 class="sujet-traite">Économie Circulaire</h4>
            <p class="auteur">Julie Tshimanga</p>
          </div>
        </div>

        <div class="carte-rapport">
          <div class="couverture-preview stage">
            <img src="https://images.unsplash.com/photo-1554774853-719586f82d77?auto=format&fit=crop&w=300" class="image-fond">
            <span class="type-badge badge-stage">STAGE</span>
          </div>
          <div class="infos-carte">
            <h4 class="sujet-traite">Finance Appliquée</h4>
            <p class="auteur">Paul Lomami</p>
          </div>
        </div>
      </div>
    </section>
  </div>


</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

// --- ÉTATS ---
const recherche = ref('')
const documents = ref([]) 
const dernierDocument = ref(null) // Stocke le dernier objet "Historique" de Django
// const BASE_URL = 'http://192.168.47.56:8000/api'
// const BASE_URL = 'http://localhost:8000/api'
const BASE_URL = 'http://192.168.189.56:8000/api'


// --- LOGIQUE DE CHARGEMENT ---
const chargerDonnees = async () => {
  try {
    // Récupération du token pour l'authentification
    const token = localStorage.getItem('access_token')
    const config = {
      headers: { Authorization: `Bearer ${token}` }
    }

    // 1. Récupérer tous les documents pour la grille
    const resDocs = await axios.get(`${BASE_URL}/documents/`, config)
    documents.value = resDocs.data

    // 2. Récupérer l'historique (Django renvoie le plus récent en premier grâce au order_by)
    const resHist = await axios.get(`${BASE_URL}/historique/`, config)
    
    if (resHist.data && resHist.data.length > 0) {
      // On prend le premier élément qui est le dernier livre ouvert
      dernierDocument.value = resHist.data[0]
    }
  } catch (e) {
    console.error("Erreur lors du chargement des données SOMA:", e)
  }
}

// --- CALCULS DYNAMIQUES ---

// Calcule le pourcentage à afficher dans la barre bleue
const progressionDynamique = computed(() => {
  if (!dernierDocument.value) return 0
  // On utilise le champ 'pourcentage_progression' calculé par le Serializer Django
  return dernierDocument.value.pourcentage_progression || 0
})

onMounted(chargerDonnees)
</script>
<!-- <script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios' -->

<!-- // Variables réactives
const recherche = ref('')
const documents = ref([]) // Liste pour ton v-for
const dernierDocument = ref(null) // Pour ta carte bleue "Reprise"

// Fonction pour charger les données depuis ton DRF
const chargerDonnees = async () => {
  try {
    const BASE_URL = 'http://192.168.47.56:8000/api' // Remplace par ton IP
    
    // 1. On récupère tous les documents
    const resDocs = await axios.get(`${BASE_URL}/documents/`)
    documents.value = resDocs.data

    // 2. On récupère le dernier historique (pour la carte bleue)
    const resHist = await axios.get(`${BASE_URL}/historique/`)
    if (resHist.data.length > 0) {
      dernierDocument.value = resHist.data[0]
    }
  } catch (e) {
    console.error("Erreur de connexion Django", e)
  }
}

// Calcul du pourcentage dynamique pour la carte bleue
const progressionDynamique = computed(() => {
  return dernierDocument.value ? dernierDocument.value.pourcentage_progression : 0
})

onMounted(chargerDonnees)
</script> -->



<style scoped>
/* Assure-toi d'avoir ces styles de base */
.conteneur-barre-progression {
  width: 100%;
  height: 8px;
  background-color: #e0e0e0; /* Gris clair pour le fond */
  border-radius: 10px;
  overflow: hidden;
  margin: 10px 0;
}

.barre-niveau-lecture {
  height: 100%;
  background-color: #2196F3; /* Bleu pour la progression */
  transition: width 0.3s ease; /* Petit effet fluide */
}
</style>