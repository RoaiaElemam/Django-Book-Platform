from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters

from .serializer import BookSerializer
from .models import Book




class BookListApi(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
  #  filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilters]
    #filterset_fields = ['title', 'job_type','vacancy']
    #search_fields = ['title', 'description']
    #ordering_fields = ['salary_start', 'salary_end','experince']


class BookDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer