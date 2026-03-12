<template>
  <div class="contenu-scroll_start">
    <div class="section-visuelle">
      <div class="cercle-animation">
        <span class="emoji-logo">🎓</span>
      </div>
      <h2 class="nom-app">SOMA</h2>
    </div>

    <div class="section-texte">
      <h1 class="titre-principal">Réussissez grâce aux travaux de vos pairs</h1>
      <p class="description-app">
        Accédez aux rapports de stage et mémoires des promotions précédentes. 
        Apprenez, inspirez-vous et progressez.
      </p>
    </div>

    <div class="section-boutons">
      <router-link to="/connexion" class="bouton-principal">Accéder à mon compte</router-link>
      <router-link to="/inscription" class="bouton-secondaire">Créer mon compte étudiant</router-link>
      </div>
      
  </div>
</template>



<script>
export default {
  name: 'CommenceView'
}
</script>

<style scoped>

</style>