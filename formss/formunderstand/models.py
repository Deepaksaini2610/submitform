from django.db import models

# Create your models here.
class bharti(models.Model):
    fname = models.CharField(max_length=50,default=True)
    lname = models.TextField(max_length=100,default=True)
    email = models.EmailField(max_length= 250,default=True)
    def __str__(self):
        return self.fname