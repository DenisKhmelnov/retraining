from django.contrib import admin

from retraining.library.models import Book, Reader, Author

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Reader)
