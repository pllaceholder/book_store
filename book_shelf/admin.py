from django.contrib import admin
from book_shelf import models
# Register your models here.


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname')


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('amount',)
