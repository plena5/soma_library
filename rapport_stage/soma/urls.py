from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

# On crée un routeur et on y enregistre nos ViewSets
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'etudiants', EtudiantViewSet)
router.register(r'facultes', FaculteViewSet)
router.register(r'departements', DepartementViewSet)
router.register(r'niveaux', NiveauViewSet)
router.register(r'documents', DocumentAcademiqueViewSet)
router.register(r'historique', HistoriqueViewSet,basename='historique')

urlpatterns = [
    
    # Routes de l'API (générées par le router)
    path('api/', include(router.urls)),
    
    # Authentification JWT
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api-auth/', include('rest_framework.urls')),  
]