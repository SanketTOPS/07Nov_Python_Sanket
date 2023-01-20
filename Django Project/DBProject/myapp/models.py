from django.db import models

# Create your models here.

class userInfo(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    dob=models.DateField()
    mobile=models.IntegerField()
    address=models.TextField()

    