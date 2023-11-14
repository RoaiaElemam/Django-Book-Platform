from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response

from .serializer import BookSerializer
from .models import Book




class BookListApi(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
  #  filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilters]
    #filterset_fields = ['title', 'job_type','vacancy']
    #search_fields = ['title', 'description']
    #ordering_fields = ['salary_start', 'salary_end','experince']


class BookDetailApi(generics.RetrieveAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer