from django.contrib import admin
from .models import *

# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('document','date_creation','nom','typeFile')

admin.site.register(Document, DocumentAdmin)

