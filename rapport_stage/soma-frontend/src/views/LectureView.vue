<template>
  <div class="contenu-mobile">
    <header class="header-lecture">
      <button @click="$router.push('/catalogue')" class="btn-retour">⬅</button>
      <h1 v-if="document">{{ document.exercice_traite }}</h1>
    </header>

    <main v-if="document" class="lecteur-container">
      <div class="infos-auteur">
        <p><strong>Institution :</strong> {{ document.institution || 'Non spécifiée' }}</p>
        <p><strong>Auteur :</strong> {{ document.auteur_nom || 'Étudiant n°' + document.auteur }}</p>
      </div>


    <div class="affichage-pdf-cadre" style="height: 1000px;width: 100%; border: 1px solid #ccc;">

      
  <iframe 
    v-if="document && document.fichier_pdf"
    :src="document.fichier_pdf" 
    width="100%" 
    height="100%" 
    style="border: none;"
    type="application/pdf"
  >
    <p>Votre navigateur ne supporte pas l'affichage direct. 
       <a :href="document.fichier_pdf" target="_blank">Ouvrir le PDF ici</a>
    </p>
  </iframe>
</div>  
<!-- 
 <div class="affichage-pdf-cadre" style="height: 600px; width: 100%;">
  <iframe 
    v-if="document.fichier_pdf"
    :src="'https://docs.google.com/viewer?url=' + encodeURIComponent(document.fichier_pdf) + '&embedded=true'" 
    width="100%" 
    height="100%" 
    style="border: none;"
  ></iframe>
</div>      -->
<!-- <div class="affichage-pdf-cadre" style="height: 600px; width: 100%;">
  <object
    v-if="document.fichier_pdf"
    :data="document.fichier_pdf"
    type="application/pdf"
    width="100%"
    height="100%"
  >
    <p>Votre navigateur ne peut pas afficher ce PDF. 
       <a :href="document.fichier_pdf">Cliquez ici pour le télécharger.</a>
    </p>
  </object>
</div> -->



      <footer class="footer-lecture">
        <div class="barre-progression">
          <div class="remplissage" :style="{ width: progression + '%' }"></div>
        </div>
        
        <div class="controles">
          <button @click="pagePrecedente" :disabled="pageActuelle <= 1">Précédent</button>
          <span class="page-info">Page {{ pageActuelle }} / {{ document.nombre_pages_total }}</span>
          <button @click="pageSuivante" :disabled="pageActuelle >= document.nombre_pages_total">Suivant</button>
        </div>
      </footer>
    </main>

    <div v-else class="loading-screen">
      <p>Chargement du document en cours...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const document = ref(null)
const pageActuelle = ref(1)
// const matriculeUtilisateur = ref('22-FS-0102') 

// Calcul de la progression en %
const progression = computed(() => {
  if (document.value && document.value.nombre_pages_total > 0) {
    return (pageActuelle.value / document.value.nombre_pages_total) * 100
  }
  return 0
})

const chargerDocument = async () => {
  const id = route.params.id
  // Utilise bien l'IP de ton serveur Django (0.0.0.0:8000)
  const BASE_URL = 'http://192.168.47.56:8000/api'
  // const BASE_URL = 'http://localhost:8000/api'
  
  try {
    // 1. Récupérer les détails du document
    const response = await axios.get(`${BASE_URL}/documents/${id}/`)
    document.value = response.data
    
    // 2. Récupérer l'historique de lecture pour cet étudiant sur ce document
    const resHist = await axios.get(`${BASE_URL}/historique/?document=${id}`)
    if (resHist.data.length > 0) {
      pageActuelle.value = resHist.data[0].page_actuelle
    }
  } catch (e) {
    console.error("Erreur API :", e)
  }
}

// Fonctions de navigation
const pageSuivante = () => { 
  if (pageActuelle.value < document.value.nombre_pages_total) {
    pageActuelle.value++
  }
}

const pagePrecedente = () => { 
  if (pageActuelle.value > 1) {
    pageActuelle.value--
  }
}

onMounted(chargerDocument)
</script>

<style scoped>
.affichage-pdf-cadre {
  position: relative;
  border: 2px solid #ddd;
  border-radius: 12px;
  overflow: hidden;
  background: #525659;
  height: 85vh;
  width: 100%;
 
} 
 


.bouclier-invisible {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 10; /* Il doit être au-dessus de l'iframe */
  background: rgba(255, 255, 255, 0); /* Totalement transparent */
  cursor: default;
}

.watermark {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(0, 0, 0, 0.3);
  color: white;
  padding: 4px 8px;
  font-size: 10px;
  z-index: 10;
  pointer-events: none;
}

.lecteur-embed {
  display: block;
}

.barre-progression {
  width: 100%;
  height: 6px;
  background: #eee;
  margin-bottom: 10px;
}

.remplissage {
  height: 100%;
  background: #3498db;
  transition: width 0.3s ease;
}

.controles {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
/* 1. Conteneur Principal (Agrandissement) */
.lecteur-container {
  width: 400px; /* Largeur confortable pour la lecture */
  margin: 0 auto;
  padding: 20px;
  background-color: rgb(249, 249, 249);
  min-height: 200vh;
  /* Protection contre le copier-coller */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
</style>
