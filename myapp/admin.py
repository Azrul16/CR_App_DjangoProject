from django.contrib import admin
from .models import Data
# Register your models here.
@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ['Course_Title', 'Course_Teacher']
    list_filter = ['date']
    search_fields = ['Course_Teacher']


