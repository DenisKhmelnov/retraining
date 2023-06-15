from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.exceptions import ValidationError

from retraining.library.validators import PhoneValidator


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
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    pages = models.IntegerField()
    quantity = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

# class Reader(BaseModel):
#     class Status(models.TextChoices):
#         ACTIVE = 'active', 'Активен'
#         INACTIVE = 'inactive', 'Неактивен'
#     name = models.CharField(max_length=255)
#     surname = models.CharField(max_length=255)
#     phone = models.CharField(max_length=12)
#     status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)
#     active_books = models.ManyToManyField(Book, related_name='readers', blank=True, max_length=3)
#     user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

class Reader(BaseModel):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Активен'
        INACTIVE = 'inactive', 'Неактивен'

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)
    active_books = models.ManyToManyField(Book, related_name='readers', blank=True, max_length=3)
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.surname

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'

