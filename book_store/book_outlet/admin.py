from django.contrib import admin
from .models import Book, Author, Country, Address

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating", )

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Country)
admin.site.register(Address)