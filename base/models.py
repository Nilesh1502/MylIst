from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CategoryModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name


class BlogModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="name")
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
