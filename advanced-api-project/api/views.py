from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# ✅ Vue pour lister tous les livres (accessible à tous)
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # ✅ Lecture seule pour non-authentifiés

# ✅ Vue pour voir un livre en détail (accessible à tous)
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # ✅ Lecture seule pour non-authentifiés

# ✅ Vue pour créer un livre (réservée aux utilisateurs authentifiés)
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Authentification requise

# ✅ Vue pour mettre à jour un livre (réservée aux utilisateurs authentifiés)
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Authentification requise

# ✅ Vue pour supprimer un livre (réservée aux utilisateurs authentifiés)
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Authentification requise
