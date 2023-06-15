from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from retraining.library.models import Author, Book, Reader
from retraining.library.permissions import IsOwner
from retraining.library.serializers import AuthorSerializer, BookSerializer, ReaderSerializer, ReaderCreateSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class ReaderViewSet(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            self.serializer_class = ReaderCreateSerializer
        return self.serializer_class

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

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsOwner | IsAdminUser]
        return [permission() for permission in permission_classes]
