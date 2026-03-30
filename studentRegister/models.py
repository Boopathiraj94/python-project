from django.db import models

# Create your models here.
class RegisterStudents(models.Model):
    fname = models.TextField()
    lname = models.TextField()
    email = models.EmailField()
    city = models.TextField()
    state = models.TextField()
    zipcode = models.IntegerField()
