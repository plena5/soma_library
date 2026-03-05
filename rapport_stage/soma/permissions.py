from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    - Lecture (GET) : Autorisée à tout utilisateur connecté.
    - Modification (POST, PUT, DELETE) : Uniquement pour le Staff/Admin.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return bool(request.user and request.user.is_staff)

class IsOwner(permissions.BasePermission):
    """
    Autorise l'accès uniquement si l'objet appartient à l'étudiant connecté.
    Utile pour l'historique et le profil personnel.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        
        # Si on vérifie un profil Etudiant
        if hasattr(obj, 'user'):
            return obj.user == request.user
        
        # Si on vérifie un Historique
        if hasattr(obj, 'etudiant'):
            return obj.etudiant.user == request.user
            
        return False