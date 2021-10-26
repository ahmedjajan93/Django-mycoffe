from django.db import models
from datetime import datetime

# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=50)
    des = models.TextField()
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    is_active = models.BooleanField( default=True)
    publish_date = models.DateTimeField(default=datetime.now)
    audio = models.FileField(upload_to='Dictionary/media', blank=True) 

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-publish_date']
    