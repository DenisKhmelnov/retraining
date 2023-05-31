from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from retraining.library.models import Author, Book, Reader
from retraining.library.serializers import AuthorSerializer, BookSerializer, ReaderSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ReaderViewSet(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
