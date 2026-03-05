from django.contrib import admin
from .models import Faculte, Departement, Niveau, Etudiant, DocumentAcademique, Historique

# 1. Gestion des Facultés
@admin.register(Faculte)
class FaculteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')
    search_fields = ('nom',)

# 2. Gestion des Départements
@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'faculte')
    list_filter = ('faculte',) 
    search_fields = ('nom',)

# 3. Gestion des Niveaux (Licence/Master)
@admin.register(Niveau)
class NiveauAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type_document')

# 4. Gestion des Étudiants
@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    # AJOUT : on affiche le département pour savoir d'où vient l'étudiant
    list_display = ('matricule', 'nom', 'prenom','faculte' ,'departement','niveau')
    # AJOUT : filtre par département pour trier les listes d'élèves
    list_filter = ('departement', 'niveau')
    search_fields = ('matricule', 'nom', 'email')
    ordering = ('nom',)

# 5. Gestion des Documents (Rapports et Mémoires)
@admin.register(DocumentAcademique)
class DocumentAcademiqueAdmin(admin.ModelAdmin):
    list_display = ('exercice_traite','institution', 'auteur', 'niveau','departement', 'date_ajout','nombre_pages_total','fichier_pdf')
    # CORRECTION : On utilise 'departement' qui est la clé étrangère réelle dans ton modèle
    list_filter = ('niveau', 'departement', 'date_ajout')
    search_fields = ('exercice_traite', 'auteur__nom', 'auteur__matricule')
    date_hierarchy = 'date_ajout' 

# 6. Historique des lectures
@admin.register(Historique)
class HistoriqueAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'document', 'page_actuelle', 'date_lecture')
    list_filter = ('date_lecture',)
    readonly_fields = ('etudiant', 'document', 'page_actuelle', 'date_lecture')