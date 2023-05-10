from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Material(models.Model):
    MATERIAL_TYPE = (
        ('theory', 'Theoretical Material'),
        ('practice', 'Practical Material')
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    body = models.TextField(max_length=1000)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    publish = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_users')
    material_type = models.CharField(max_length=200, choices=MATERIAL_TYPE)


    def __str__(self):
        return self.title