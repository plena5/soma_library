<template>
  <div class="contenu-mobile-app contenu-scroll">
    <header class="header-accueil">
      <div class="infos-utilisateur">
        <span class="salutation">Mon Espace</span>
        <h1 class="titre-section">Ma Bibliothèque</h1>
        <div class="phrase-inspiration">
          <p>"L'éducation est l'arme la plus puissante pour changer le monde."</p>
        </div>
      </div>
      <div class="logo-mini-rouge">📚</div>
    </header>

    <section class="section-reprise">
      <h2 class="sous-titre">Continuer la lecture</h2>
      <div class="carte-bleue-reprise">
        <div class="contenu-reprise">
          <span class="badge-status">EN COURS</span>
          <h2 class="titre-livre-reprise">Audit de Sécurité IT</h2>
          <p class="auteur-livre-reprise">Par Sarah Mutombo</p>
          <div class="conteneur-barre-progression">
            <div class="barre-niveau-lecture" :style="{ width: '85%' }"></div>
          </div>
          <span class="info-pourcentage">85% terminé</span>
        </div>
        <router-link to="/lecture" class="bouton-lecture-directe">▶</router-link>
      </div>
    </section>

    <section class="section-historique">
      <div class="flex-titre">
        <h2 class="sous-titre">Historique récent</h2>
        <button @click="effacerHistorique" class="btn-lien-rouge">Effacer</button>
      </div>

      <div class="liste-historique">
        <div class="item-historique">
          <div class="mini-couverture">
            <img src="https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=100">
          </div>
          <div class="infos-historique">
            <h4 class="titre-doc">Marketing Digital V2</h4>
            <p class="date-consultation">Consulté hier</p>
          </div>
          <div class="statut-lu">✅</div>
        </div>

        <div class="item-historique">
          <div class="mini-couverture">
            <img src="https://images.unsplash.com/photo-1454165833767-027508496b41?auto=format&fit=crop&w=100">
          </div>
          <div class="infos-historique">
            <h4 class="titre-doc">Économie Circulaire</h4>
            <p class="date-consultation">Consulté le 12 Fév.</p>
          </div>
          <div class="statut-lu">✅</div>
        </div>

        <div class="item-historique">
          <div class="mini-couverture">
            <img src="https://images.unsplash.com/photo-1554774853-719586f82d77?auto=format&fit=crop&w=100">
          </div>
          <div class="infos-historique">
            <h4 class="titre-doc">Finance Appliquée</h4>
            <p class="date-consultation">Consulté le 10 Fév.</p>
          </div>
          <div class="statut-lu">✅</div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Ma_bibliothequeView',
  methods: {
    effacerHistorique() {
      if(confirm("Voulez-vous vraiment effacer votre historique ?")) {
        console.log("Historique effacé");
        // Logique pour vider la liste plus tard
      }
    }
  }
}
</script>

<style scoped>


</style>