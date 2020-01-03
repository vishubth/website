from django.db import models


# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.email
