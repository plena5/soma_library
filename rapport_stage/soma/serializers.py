from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Faculte, Departement, Niveau, Etudiant, DocumentAcademique, Historique

# 1. Gestion des Utilisateurs
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff']

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'

class FaculteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculte
        fields = '__all__'

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = '__all__'
class NiveauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveau
        fields = '__all__'

class DocumentAcademiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentAcademique
        fields = '__all__'

class HistoriqueSerializer(serializers.ModelSerializer):
    # Récupère le titre et l'auteur depuis le document lié
    document_titre = serializers.ReadOnlyField(source='document.exercice_traite')
    auteur_nom = serializers.ReadOnlyField(source='document.etudiant.nom')
    
    # Indique explicitement d'inclure la @property du modèle
    pourcentage_progression = serializers.ReadOnlyField()

    class Meta:
        model = Historique
        fields = [
            'id', 'etudiant', 'document', 'document_titre', 
            'auteur_nom', 'page_actuelle', 'pourcentage_progression', 'date_lecture'
        ]

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['is_staff'] = self.user.is_staff
        
        # Si l'utilisateur est un étudiant, on peut aussi renvoyer son matricule
        try:
            etudiant = Etudiant.objects.get(user=self.user)
            data['matricule'] = etudiant.matricule
        except Etudiant.DoesNotExist:
            data['matricule'] = None
            
        return data