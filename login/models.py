from django.db import models

# Create your models here.


class users(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.username} {self.email} {self.pwd}'
