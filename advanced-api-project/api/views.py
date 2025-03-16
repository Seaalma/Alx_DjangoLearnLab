from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# ✅ Liste des livres (GET) et ajout d'un livre (POST)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions: Lecture pour tous, écriture pour les utilisateurs authentifiés
    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return []

# ✅ Détails d'un livre (GET), mise à jour (PUT/PATCH) et suppression (DELETE)
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions: Lecture pour tous, modifications pour les utilisateurs authentifiés
    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [permissions.IsAuthenticated()]
        return []

