from django.db import models

# Create your models here.


class Images(models.Model):
   upload_by = models.CharField(max_length=70)
   upload_at = models.DateField(auto_now_add=True)
   image     = models.ImageField(upload_to='Images/')