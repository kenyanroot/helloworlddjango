from django.db import models

# Create your models here.
class Namecomment(models.Model):
    comment=models.TextField(blank=True)
    phone_number=models.CharField(max_length=12 )
    name=models.TextField(blank= True)

