from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Author(BaseModel):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='authors', null=True, blank=True)

    def __str__(self):
        return self.name


class Book(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    pages = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

class Reader(BaseModel):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Активен'
        INACTIVE = 'inactive', 'Неактивен'
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = PhoneNumberField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)
    active_books = models.ManyToManyField(Book, related_name='readers', blank=True, max_length=3)


