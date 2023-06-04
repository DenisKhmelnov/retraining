from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from retraining.library.models import Author, Book, Reader
from retraining.library.validators import PhoneValidator


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ["id",
                  "name",
                  "surname",
                  "picture"
                  ]


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ["id",
                  "title",
                  "description",
                  "pages",
                  "quantity",
                  "author"
                  ]


class ReaderSerializer(ModelSerializer):
    phone = serializers.CharField(validators=[PhoneValidator()])
    class Meta:
        model = Reader
        fields = [
            "id",
            "name",
            "surname",
            "phone",
            "status",
            "active_books"
            ]
