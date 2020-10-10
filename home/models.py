from django.db import models

# Create your models here.
class Contact(models.Model):
    message_title=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    desc=models.TextField()
    date=models.CharField(max_length=255)

    def __str__(self):
        return self.message_title

class blog(models.Model):
    Name=models.CharField(max_length=255)
    Desc=models.TextField()
    Slug=models.CharField(max_length=255)
    Date=models.DateField(max_length=255)

    def __str__(self):
        return self.Name