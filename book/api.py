from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters

from .serializer import BookSerializer
from .models import Book




class BookListApi(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'price','author']
    search_fields = ['title']
    ordering_fields = ['price', 'publish_date']


class BookDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer