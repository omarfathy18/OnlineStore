from django.db import models

# Create your models here.


class items(models.Model):
    p_name = models.CharField(max_length=50)
    p_price = models.IntegerField()
    p_img = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.p_name} {self.p_price} {self.p_img}'
