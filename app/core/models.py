from django.db import models
from django.contrib.postgres.validators import RangeMinValueValidator, RangeMaxValueValidator

# Create your models here.


class Hall(models.Model):
    name = models.CharField(max_length=100, verbose_name="Hall name")

class Table(models.Model):

    SHAPE_CHOICES = [
        ('s', 'square'),
        ('o', 'oval')
    ]

    number = models.IntegerField(verbose_name="Number table")
    seats_count =  models.IntegerField(verbose_name="Number of seats")
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    shape = models.CharField(
        max_length=100,
        choices=SHAPE_CHOICES
        verbose_name="Hall name"
    )
    horizontal_coordinates = models.IntegerRangeField(
        validators=[
            RangeMinValueValidator(1),
            RangeMaxValueValidator(100)
        ],
        verbose_name="Horizontal coordinates" )
    vertical_coordinates = models.IntegerRangeField(
        validators=[
            RangeMinValueValidator(1),
            RangeMaxValueValidator(100)
        ],
        verbose_name="Vertical coordinates")

    width = models.IntegerRangeField(
        validators=[
            RangeMinValueValidator(1),
            RangeMaxValueValidator(100)
        ],
        verbose_name="Width table")
    height = models.IntegerRangeField(
        validators=[
            RangeMinValueValidator(1),
            RangeMaxValueValidator(100)
        ],
        verbose_name="Height table")


class Order(models.Model):
    name_customer = models.CharField(max_length=450, verbose_name="Name customer")
    date = models.DataField(auto_now=True, verbose_name="Order date")
    number_table = models.IntegerField(verbose_name="Number table")
    email_address = models.EmailField(verbose_name="Email customer")
