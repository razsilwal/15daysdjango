from django.db import models
# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length=25)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


