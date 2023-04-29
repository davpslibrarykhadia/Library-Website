from django.db import models
from pickle import TRUE
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Home(models.Model):
    Sno = models.AutoField(primary_key=True)
    image = models.TextField(max_length=100)
    line_1 = models.TextField()
    line_2 = models.TextField()
    line_3 = models.TextField()
    
    def str(self) -> str:
        return "Posted by "+ self.image + " - " 

class AboutCorousel(models.Model):
    image = models.CharField(max_length=100)
    position = models.IntegerField()

class AboutText(models.Model):
    Sno = models.AutoField(primary_key=True)
    text = models.TextField()

class AboutLibrarian(models.Model):
    Sno = models.AutoField(primary_key=True)
    image = models.CharField(max_length=100)
    text = models.TextField()
    title = models.CharField(max_length=150)   

class BooksNewArrival(models.Model):
    image = models.CharField(max_length=100)
    position = models.IntegerField()

class BooksTopPicks(models.Model):
    image = models.CharField(max_length=100)
    position = models.IntegerField()

class ContactDetails(models.Model):
    Sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.CharField(max_length=100)


class Notice(models.Model):
    Sno = models.AutoField(primary_key=True)
    notice = models.TextField()



