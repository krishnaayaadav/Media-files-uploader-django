from django.contrib import admin
from .models import Images

@admin.register(Images)
class ImageModel(admin.ModelAdmin):
   list_display = ('id', 'upload_by', 'upload_at', 'image')