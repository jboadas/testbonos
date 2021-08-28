from django.db import models
from django.core.validators import (
    MinLengthValidator,
    MinValueValidator,
    MaxValueValidator)


class Bonos(models.Model):
    bono_id = models.AutoField(primary_key=True)
    bono_name = models.CharField(
        max_length=40,
        validators=[MinLengthValidator(4)],
        blank=False)
    bono_number = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10000)])
    bono_price = models.DecimalField(max_digits=9, decimal_places=4)

    class Meta:
        ordering = ['bono_id']
