from django.db import models
from django.contrib.auth.models import User
from django.core.validators import (
    MinLengthValidator,
    MinValueValidator,
    MaxValueValidator)


# python manage.py makemigrations mainbonos
# python manage.py migrate

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
    created_by = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING)
    bought_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name='auth_user_id')

    class Meta:
        ordering = ['bono_id']
