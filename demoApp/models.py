from django.db import models


# Create your models here.

class Status(models.Model):
    Status = models.CharField(max_length=50)

class Master(models.Model):
    Status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
    
    Name = models.CharField(max_length=25)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=25)

class chkboxcourse(models.Model):
    coursename = models.CharField(max_length=50)
