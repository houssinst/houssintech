from django.db import models

class Project(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=150)
    technology = models.CharField(max_length=40)
    description = models.TextField(max_length=400)
    
   
