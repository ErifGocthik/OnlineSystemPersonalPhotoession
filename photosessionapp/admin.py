from django.contrib import admin

# Register your models here.
from photosessionapp.models import Photographer, Review, CustomUser


@admin.register(Photographer)
class PhotographerAdmin(admin.ModelAdmin):
    exclude = ['id']
    list_display = ['clearUsername']
    search_fields = ['clearUsername']


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    exclude = ['id']
    list_display = ['username', 'name', 'surname', 'user_type']
    list_filter = ['user_type']
    search_fields = ['username', 'name', 'surname']


@admin.register(Review)
class Review(admin.ModelAdmin):
    exclude = ['id']
    list_display = ['Username', 'text_content']
    list_filter = ['likes']
    search_fields = ['text_content']
