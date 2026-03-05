from django.shortcuts import render

# Create your views here.
def home (request):
    return render ( request,'home.html')


from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import action
from django.http import FileResponse
from .models import *
from .serializers import *
from .permissions import IsOwner, IsAdminOrReadOnly
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response

# 1. AUTHENTIFICATION
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# 2. UTILISATEURS (Admin seulement)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

# # 3. ETUDIANTS (Remplace Habitant)
# class EtudiantViewSet(viewsets.ModelViewSet):
    # queryset = Etudiant.objects.all()
    # serializer_class = EtudiantSerializer
    # filter_backends = [DjangoFilterBackend]
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [AllowAny]


    # permission_classes = [IsAuthenticated]
    
    # @action(detail=False, methods=['get'])
    # def me(self, request):
    #     try:
        #      Grâce à IsAuthenticated, request.user est forcément un utilisateur réel ici
        #     etudiant = Etudiant.objects.get(user=request.user)
            
        #     data = {
        #         "nom": etudiant.nom,
        #         "prenom": etudiant.prenom,
        #         "email": etudiant.email,
        #         "telephone": etudiant.telephone,
        #         "matricule": etudiant.matricule,
        #         "faculte": etudiant.faculte.nom if etudiant.faculte else "N/A",
        #         "departement": etudiant.departement.nom if etudiant.departement else "N/A",
        #         "niveau": etudiant.niveau.nom if etudiant.niveau else "N/A",
        #     }
        #     return Response(data)
        # except Etudiant.DoesNotExist:
        #     return Response({"error": "Profil étudiant non trouvé"}, status=404)
# 4. FACULTES (Remplace Categorie)
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from django.db import transaction
from .models import Etudiant
from .serializers import EtudiantSerializer

class EtudiantViewSet(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    filter_backends = [DjangoFilterBackend]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] # Cadenas par défaut

    # 1. ACTION D'INSCRIPTION (Porte Ouverte)
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def inscription(self, request):
        data = request.data
        try:
            with transaction.atomic():
                # Créer l'utilisateur Django (le login)
                user = User.objects.create_user(
                    username=data['matricule'],
                    email=data['email'],
                    password=data['password'],
                    first_name=data.get('prenom', ''),
                    last_name=data.get('nom', '')
                )

                # Créer le profil Etudiant lié
                Etudiant.objects.create(
                    user=user,
                    nom=data['nom'],
                    prenom=data['prenom'],
                    email=data['email'],
                    telephone=data['telephone'],
                    matricule=data['matricule'],
                    faculte_id=data['faculte'], # Reçoit l'ID (ex: 1)
                    departement_id=data['departement'],
                    niveau_id=data['niveau']
                )
            return Response({"message": "Inscription réussie !"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            # Si le matricule existe déjà ou autre erreur
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # 2. ACTION PROFIL (Cadenas IsAuthenticated)
    @action(detail=False, methods=['get'])
    def me(self, request):
        try:
            etudiant = Etudiant.objects.get(user=request.user)
            data = {
                "nom": etudiant.nom,
                "prenom": etudiant.prenom,
                "email": etudiant.email,
                "telephone": etudiant.telephone,
                "matricule": etudiant.matricule,
                "faculte": etudiant.faculte.nom if etudiant.faculte else "N/A",
                "departement": etudiant.departement.nom if etudiant.departement else "N/A",
                "niveau": etudiant.niveau.nom if etudiant.niveau else "N/A",
            }
            return Response(data)
        except Etudiant.DoesNotExist:
            return Response({"error": "Profil étudiant non trouvé"}, status=404)
class FaculteViewSet(viewsets.ModelViewSet):
    queryset = Faculte.objects.all()
    serializer_class = FaculteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'nom': ['icontains']}
    # permission_classes = [IsAdminOrReadOnly]
    permission_classes = [AllowAny]


# 5. DEPARTEMENTS
class DepartementViewSet(viewsets.ModelViewSet):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'nom': ['icontains'],
        'faculte': ['exact'],
    }
    # permission_classes = [IsAdminOrReadOnly]
    permission_classes = [AllowAny]
class NiveauViewSet(viewsets.ModelViewSet):
    queryset = Niveau.objects.all()
    serializer_class = NiveauSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'nom': ['icontains']}
    # permission_classes = [IsAdminOrReadOnly]
    permission_classes = [AllowAny]

# 6. DOCUMENTS ACADEMIQUES (Remplace Ouvrage)
class DocumentAcademiqueViewSet(viewsets.ModelViewSet): 
    queryset = DocumentAcademique.objects.all()
    serializer_class = DocumentAcademiqueSerializer
    filter_backends = [DjangoFilterBackend]
    # permission_classes = [IsAdminOrReadOnly]
    permission_classes = [AllowAny]
    filterset_fields = {
        'exercice_traite': ['icontains'], 
        'auteur__nom': ['icontains'], # Recherche par nom de l'étudiant
        'departement': ['exact'],
        'departement__faculte': ['exact'], # Filtrer par Faculté entière
        'niveau': ['exact'],
        'date_ajout': ['gte', 'lte'],
    }
    @method_decorator(xframe_options_exempt) # ✅ CETTE LIGNE DÉBLOQUE L'IFRAME
    @action(detail=True, methods=['get'])
    def lire(self, request, pk=None):
        document = self.get_object()
        response = FileResponse(document.fichier_pdf, content_type='application/pdf')
        
        # 'inline' est parfait ici pour l'affichage
        response['Content-Disposition'] = f'inline; filename="doc_{document.id}.pdf"'
        
        # On peut aussi forcer le header ici par sécurité
        response['X-Frame-Options'] = 'ALLOWALL' 
        
        return response


#     @action(detail=True, methods=['get'])
#     def lire(self, request, pk=None):
#         document = self.get_object()
#         response = FileResponse(document.fichier_pdf, content_type='application/pdf')
#         response['Content-Disposition'] = f'inline; filename="doc_{document.id}.pdf"'
#         return response
# # On ajoute ce décorateur sur la méthode qui récupère le document
#     @xframe_options_exempt
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
# 7. HISTORIQUE (Remplace SuiviLecture)
# class HistoriqueViewSet(viewsets.ModelViewSet):
#     queryset = Historique.objects.all()
#     serializer_class = HistoriqueSerializer
#     filter_backends = [DjangoFilterBackend]
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated, IsOwner]
    # filterset_fields = {
    #     'document': ['exact'],
    #     'date_lecture': ['gte', 'lte'],
    # }
class HistoriqueViewSet(viewsets.ModelViewSet):
        queryset = Historique.objects.all()
        serializer_class = HistoriqueSerializer
        permission_classes = [IsAuthenticated]

        def get_queryset(self):
        # On renvoie l'historique de l'étudiant connecté, le plus récent en haut
          return Historique.objects.filter(etudiant__user=self.request.user).order_by('-date_lecture')

        @action(detail=False, methods=['post'])
        def enregistrer_page(self, request):
            doc_id = request.data.get('document_id')
            page = request.data.get('page')
          
        # On récupère le profil de l'étudiant connecté
            etudiant = Etudiant.objects.get(user=request.user)
        
        # Met à jour la page si l'historique existe, sinon le crée
            obj, created = Historique.objects.update_or_create(
            etudiant=etudiant,
            document_id=doc_id,
            defaults={'page_actuelle': page}
        )
        
            return Response({
            'status': 'Page enregistrée',
            'pourcentage': obj.pourcentage_progression
        })