from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
]
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        # Exemple de validation personnalisée (peut être adaptée selon ton modèle)
        if serializer.validated_data["title"].lower() == "forbidden":
            raise serializers.ValidationError({"title": "Ce titre est interdit"})
        serializer.save()
