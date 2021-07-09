from django.contrib import admin
from .models import CategoryModel, BlogModel
# Register your models here.
admin.site.register(CategoryModel)
admin.site.register(BlogModel)
