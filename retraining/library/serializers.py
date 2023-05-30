from rest_framework.serializers import ModelSerializer

from retraining.library.models import Author, Book, Reader


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
