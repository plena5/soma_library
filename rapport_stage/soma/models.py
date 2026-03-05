import fitz  # PyMuPDF
from django.core.files.base import ContentFile
from django.db import models
from django.contrib.auth.models import User


# 1. STRUCTURE ADMINISTRATIVE (Les 9 facultés)
class Faculte(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class Departement(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    faculte = models.ForeignKey(Faculte, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} "

class Niveau(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50) # Ex: "Licence", "Master"
    type_document = models.CharField(max_length=50) # Ex: "Rapport de Stage", "Mémoire"

    def __str__(self):
        return f"{self.nom}"

# 3. L'ÉTUDIANT
class Etudiant(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    matricule = models.CharField(max_length=50, unique=True)
    faculte= models.ForeignKey(Faculte, on_delete=models.PROTECT)    # L'étudiant est lié à un niveau actuel (ex: il est en Master)
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)    # L'étudiant est lié à un niveau actuel (ex: il est en Master)
    niveau = models.ForeignKey(Niveau, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.matricule})"

class DocumentAcademique(models.Model):
    id = models.BigAutoField(primary_key=True)
    exercice_traite = models.CharField(max_length=255)
    institution = models.CharField(max_length=255, null=True, blank=True)
    auteur = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete=models.PROTECT) # Rapport vs Mémoire
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    date_ajout = models.DateTimeField(auto_now_add=True)
    fichier_pdf = models.FileField(upload_to='documents_pdf/')
    nombre_pages_total = models.PositiveIntegerField(default=0, editable=False)

    def save(self, *args, **kwargs):
        # Si un fichier est présent, on compte les pages automatiquement
        if self.fichier_pdf:
            try:
                # Lecture en mémoire
                pdf_bytes = self.fichier_pdf.read()
                pdf = fitz.open(stream=pdf_bytes, filetype="pdf")
                
                # On récupère le nombre de pages
                self.nombre_pages_total = len(pdf)
                
                pdf.close()
                # On remet le fichier à l'état initial pour l'enregistrement disque
                self.fichier_pdf.seek(0)
            except Exception as e:
                print(f"Erreur automatique : {e}")
        
        # Enregistrement final
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.niveau.type_document} : {self.exercice_traite}"

# 5. HISTORIQUE & PROGRESSION
class Historique(models.Model):
    id = models.BigAutoField(primary_key=True)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    document = models.ForeignKey(DocumentAcademique, on_delete=models.CASCADE)
    date_lecture = models.DateTimeField(auto_now=True)
    page_actuelle = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('etudiant', 'document')

    @property
    def pourcentage_progression(self):
        if self.document.nombre_pages_total > 0:
            pourcentage = (self.page_actuelle / self.document.nombre_pages_total) * 100
            return min(int(pourcentage), 100)
        return 0
    
    