from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book, Favorite
from .serializers import BookSerializer
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .recommendations import get_recommendations

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'authors__name']

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def recommendations(self, request):
        recommended_books = get_recommendations(request.user)
        serializer = self.get_serializer(recommended_books, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def add_to_favorites(self, request, pk=None):
        try:
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        request.user.favorite_books.add(book)

        recommended_books = get_recommendations(request.user)
        serializer = self.get_serializer(recommended_books, many=True)
        
        return Response({
            "status": "Book added to favorites",
            "recommended_books": serializer.data
        }, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def remove_from_favorites(self, request, pk=None):
        try:
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        request.user.favorite_books.remove(book)
        return Response({"status": "Book removed from favorites"}, status=status.HTTP_200_OK)