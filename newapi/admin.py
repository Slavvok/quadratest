from django.contrib import admin
from .models import TextUpload

class TextUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')

admin.site.register(TextUpload, TextUploadAdmin)
