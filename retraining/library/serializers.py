from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from retraining.library.models import Author, Book, Reader
from retraining.library.validators import PhoneValidator, PagesValidator


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ["id",
                  "name",
                  "surname",
                  "picture"
                  ]


class BookSerializer(ModelSerializer):
    pages = serializers.IntegerField(validators=[PagesValidator()])
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
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    phone = serializers.CharField(validators=[PhoneValidator()])

    class Meta:
        model = Reader
        fields = [
            "id",
            "name",
            "surname",
            "phone",
            "status",
            "active_books",
            "user"
            ]


class ReaderCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)
    phone = serializers.CharField(validators=[PhoneValidator()])

    class Meta:
        model = Reader
        fields = [
            "name",
            "surname",
            "phone",
            "status",
            "active_books",
            "username",
            "password"
        ]

    def create(self, validated_data):
        # Создание пользователя
        username = validated_data.get('username')
        password = validated_data.get('password')
        user = User.objects.create_user(username=username, password=password)

        # Создание читателя
        reader = Reader.objects.create(
            user=user,
            name=validated_data.get('name'),
            surname=validated_data.get('surname'),
            phone=validated_data.get('phone'),
            status=validated_data.get('status')
        )

        # Добавление активных книг
        active_books = validated_data.get('active_books')
        for book in active_books:
            reader.active_books.add(book)

        return reader

