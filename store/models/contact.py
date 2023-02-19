from datetime import date
from django.db import models

class Contact(models.Model):
    
    name = models.CharField(max_length=30)
    phone = models.IntegerField(default=100)
    email = models.CharField(max_length=30,default='name@gmail.com')
    description = models.CharField(max_length=500)
    # date = date.DateField()
 
    
