from django.shortcuts import render
from rest_framework import serializers
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

    def perform_create(self, serializer):
        books = serializer.validated_data.get('active_books')
        for book in books:
            if book.quantity <= 0:
                raise serializers.ValidationError("Книга недоступна в данный момент.")
        serializer.save()

    def perform_update(self, serializer):
        books = serializer.validated_data.get('active_books')
        for book in books:
            if book.quantity <= 0:
                raise serializers.ValidationError("Книга недоступна в данный момент.")
        serializer.save()

