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


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']


class ReaderCreateSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()
    phone = serializers.CharField(validators=[PhoneValidator()])

    class Meta:
        model = Reader
        fields = [
            'id',
            'name',
            'surname',
            'phone',
            'status',
            'active_books',
            'user',
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        books = validated_data.pop('active_books', [])
        user = User.objects.create_user(password=password, **user_data)
        reader = Reader.objects.create(user=user, **validated_data)
        reader.active_books.set(books)
        return reader
