from django.db import models

# Create your models here.
from datetime import date
from enum import Enum
from decimal import Decimal
import calendar


# Create your models here.
class MenuChoice(Enum):
    """Scelte possibili per i nomi del Menu"""
    PR = "Primo"
    SC = "Secondo"
    CN = "Contorno"
    DS = "Dessert"

class Service(models.Model):
    name = models.CharField(
        max_length = 10,
        choices = [(tag, tag.value) for tag in MenuChoice])

    def __str__(self):
        return self.name


class Plates(models.Model):

    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_menu = models.BooleanField(default=False)
    menu_name = models.ForeignKey('Service',models.CASCADE) # related_name='menu')

    def __str__(self):
        return self.name


class WeekDay(Enum):
    """Giorni della settimana"""
    MON = "Monday"
    TUE = "Tuesday"
    WED = "Wednesday"
    THU = "Thursday"
    FRI = "Friday"
    SAT = "Saturday"
    SUN = "Sunday"


def weekdays(day):
    id = 0
    for d in Day.objects.filter(d=day):
        id = d.pk

    return id


class Day(models.Model):
    d = models.CharField(
        max_length = 10,
        choices =[(tag, tag.value) for tag in WeekDay],#(calendar.day_name[date.today().weekday()])
        )

    def __str__(self):
        return self.d


#Ordine dell user
class Employee(models.Model):

    name = models.CharField(max_length=30)
    date = models.ForeignKey('Day',models.CASCADE)
    total = models.DecimalField(max_digits=8, decimal_places=2,default=Decimal('0.00'))
    plate_chosen = models.ManyToManyField('Plates')
