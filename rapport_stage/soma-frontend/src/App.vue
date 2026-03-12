<template>
  <div id="app-conteneur">
    <div :class="{ 'contenu-scroll': afficherMenu }">
      <router-view />
    </div>

    <nav v-if="afficherMenu" class="bottom-nav">
      <router-link to="/home" class="nav-item">
        🏠<span>Accueil</span>
      </router-link>
      
      <router-link to="/catalogue" class="nav-item">
        📂<span>Catalogue</span>
      </router-link>
      
      <router-link to="/ma-bibliotheque" class="nav-item">
        📖<span>Biblio</span>
      </router-link>
      
      <router-link to="/profil" class="nav-item">
        👤<span>Profil</span>
      </router-link>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'App',
  computed: {
    // Cette fonction vérifie le nom de la route actuelle définie dans router/index.js
    afficherMenu() {
      // Liste des pages où l'on NE VEUT PAS de menu (Bienvenue et Auth)
      const routesSansMenu = ['start', 'connexion', 'inscription'];
      
      // On vérifie si le nom de la route actuelle est dans la liste
      return !routesSansMenu.includes(this.$route.name);
    }
  }
}
</script>

<style>
/* 1. IMPORT DE TON CSS GLOBAL */
@import "./assets/style.css";

/* 2. STRUCTURE DU CONTENEUR */
 #app-conteneur {
  max-width: 100%; 
  margin: 0 auto;
  min-height: 100vh;
  position: relative;
  background-color: #fff;
 /* On s'assure que le contenu prend toute la place * */
  display: flex;
  flex-direction: column;
}

/* /3. STYLE DE LA BARRE DE NAVIGATION  */
.bottom-nav {
  position: fixed; 
  bottom: 0;
  left: 0;
  width: 100%;
  height: 65px;
  display: flex;
  justify-content: space-around;
  align-items: center;
  background: rgb(221, 6, 6);
  border-top: 1px solid #eee;
  z-index: 1000;
  box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
}

.nav-item {
  text-decoration: none;
  color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 30px;
  transition: all 0.2s ease;
  flex: 1;
} */

.nav-item span {
  margin-top: 4px;
}

/* 4. ÉTAT ACTIF (ROUGE SOMA) * Vue Router ajoute automatiquement cette classe au lien cliqué */
.nav-item.router-link-active {
  color: #0e37f1;
  font-weight: bold;
}

/* /* 5. ESPACEMENT POUR LE SCROLL * */
.contenu-scroll {
   /* On laisse de la place en bas pour ne pas que le menu cache le contenu * */
  padding-bottom: 80px; 
}
</style>