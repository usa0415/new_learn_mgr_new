from django.contrib import admin
from .models import leraning_time

# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'startdt', 'category')
    search_fields = ['category']

admin.site.register(leraning_time,DataAdmin)

