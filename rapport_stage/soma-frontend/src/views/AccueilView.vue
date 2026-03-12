<template>
  <div class="contenu-mobile-app contenu-scroll">
    <header class="header-accueil">
      <div class="infos-utilisateur">
        <h1 class="titre-section">SOMA Library</h1>
      </div>
      <div class="logo-mini-rouge">🎓</div>
    </header>

    <div class="hero-inspiration">
      <div class="overlay-hero">
        <h2>Réussissez votre travail de fin d'études</h2>
        <p>Inspirez-vous des meilleurs mémoires et rapports de stage de votre faculté.</p>
        <br>
        <router-link to="/catalogue" class="bouton-connexion-rouge">
          COMMENCER À EXPLORER
        </router-link>
      </div>
    </div>

    <section class="section-galerie">
      <div class="flex-titre">
        <h2 class="sous-titre">Rapports de stage</h2>
        <router-link to="/catalogue" class="lien-rouge">Tout voir</router-link>
      </div>
      <div class="scroll-couvertures">
        <div class="carte-rapport">
          <div class="couverture-preview memoire">
            <img src="https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&w=300" class="image-fond">
            <span class="type-badge">Stage</span>
          </div>
          <div class="infos-carte">
            <h4 class="sujet-traite">Optimisation logistique</h4>
            <p class="auteur">David Kabeya</p>
          </div>
        </div>
    <div class="carte-rapport">
          <div class="couverture-preview memoire">
            <img src="https://images.unsplash.com/photo-1532094349884-543bc11b234d?auto=format&fit=crop&w=300" class="image-fond">
            <span class="type-badge">Stage</span>
          </div>
          <div class="infos-carte">
            <h4 class="sujet-traite">Microbiologie Clinique</h4>
            <p class="auteur">Dr. Marie Noella</p>
          </div>
        </div>
        <div class="carte-rapport">
                    <div class="couverture-preview memoire">
                        <img src="https://images.unsplash.com/photo-1505664194779-8beaceb93744?auto=format&fit=crop&w=300" class="image-fond">
                        <span class="type-badge">MÉMOIRE</span>
                    </div>
                    <div class="infos-carte">
                        <h4 class="sujet-traite">Urbanisme Durable</h4>
                        <p class="auteur">Isaac Tshilombo</p>
                    </div>
                </div>
      </div>
    </section>

    <section class="section-galerie">
      <div class="flex-titre">
        <h2 class="sous-titre">Mémoires de Recherche</h2>
        <router-link to="/catalogue" class="lien-rouge">Tout voir</router-link>
      </div>
      <div class="scroll-couvertures">
        <div class="carte-rapport">
          <div class="couverture-preview memoire">
            <img src="https://images.unsplash.com/photo-1505664194779-8beaceb93744?auto=format&fit=crop&w=300" class="image-fond">
            <span class="type-badge">MÉMOIRE</span>
          </div>
          <div class="infos-carte">
            <h4 class="sujet-traite">Urbanisme Durable</h4>
            <p class="auteur">Isaac Tshilombo</p>
          </div>
        </div>
        <div class="carte-rapport">
                    <div class="couverture-preview memoire">
                        <img src="https://images.unsplash.com/photo-1505664194779-8beaceb93744?auto=format&fit=crop&w=300" class="image-fond">
                        <span class="type-badge">MÉMOIRE</span>
                    </div>
                    <div class="infos-carte">
                        <h4 class="sujet-traite">Urbanisme Durable</h4>
                        <p class="auteur">Isaac Tshilombo</p>
                    </div>
                </div>
      </div>
    </section>
  </div>
</template>

<script >

// import {ref} from 'vue'
// const prenom = ref ('oriana')
</script>

<style scoped>

/* On peut ajouter ici les styles spécifiques au Hero ou aux sliders s'ils ne sont pas dans style.css  */
.hero-inspiration {
  border-radius: 15px;
  overflow: hidden;
  margin: 10px;
  background-image: url('https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=800');
  background-size: cover;
  color: white;
}
.overlay-hero {
  background: rgba(0, 0, 0, 0.5);
  padding: 30px 20px;
}
</style>