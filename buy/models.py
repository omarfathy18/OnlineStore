from django.db import models

# Create your models here.


class buy(models.Model):
    email = models.CharField(max_length=50)
    p_name = models.CharField(max_length=50)
    p_price = models.IntegerField()
    p_state = models.SmallIntegerField(default=0)
    p_quantity = models.IntegerField()
    p_total = models.IntegerField()
    p_img = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.p_name} {self.p_price} {self.p_state} {self.p_quantity} {self.p_total} {self.p_img}'
