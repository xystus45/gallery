from django.contrib import admin
from .models import Picture, tags, Category
# Register your models here.

admin.site.register(Picture)
admin.site.register(tags)
admin.site.register(Category)