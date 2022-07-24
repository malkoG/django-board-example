from boards.models import Board
from django.contrib import admin


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['title']
