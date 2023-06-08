from django.contrib import admin
from django.db.models import QuerySet
from django.urls import reverse
from django.utils.html import format_html

from retraining.library.models import Book, Reader, Author

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'author_link', 'quantity')
    list_display_links = ('title',)
    actions = ('set_quantity_to_zero',)

    def author_link(self, obj):
        url = reverse("admin:library_author_change", args=[obj.author.id])
        return format_html('<a href="{}">{}</a>', url, obj.author)

    author_link.short_description = 'Author'

    @admin.action(description="Установить количество в ноль")
    def set_quantity_to_zero(self, request, qs: QuerySet):
        qs.update(quantity=0)

class ReaderAdmin(admin.ModelAdmin):
    list_display = ('id','name','surname','phone','status')
    list_filter = ('status',)
    actions = ('change_status', 'remove_all_books')

    @admin.action(description="Изменить статус участника")
    def change_status(self, request, qs: QuerySet):
        for reader in qs:
            reader.status = Reader.Status.ACTIVE\
                if reader.status == Reader.Status.INACTIVE\
                else Reader.Status.INACTIVE
            reader.save()

    @admin.action(description="Удалить все книги у читателя")
    def remove_all_books(self, request, queryset):
        for reader in queryset:
            reader.active_books.clear()

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'picture')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Reader, ReaderAdmin)
