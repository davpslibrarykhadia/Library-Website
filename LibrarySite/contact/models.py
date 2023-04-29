from django.db import models
from django.utils.timezone import now

# Create your models here.
class Contact(models.Model):
    Sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=140)
    Timestamp = models.DateTimeField(default=now)
    message = models.TextField()


    def _str_(self) -> str:
        return "Posted by "+ self.name + " - " + self.subject
