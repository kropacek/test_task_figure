from django.db import models

from .enums import BoardNumberChoices, ModelChoices


class Truck(models.Model):
    board_number = models.CharField(max_length=8, choices=BoardNumberChoices.choices, unique=True)
    model = models.CharField(max_length=20, choices=ModelChoices.choices)
    max_load = models.FloatField()
    current_load = models.FloatField()
    unload_coordinates = models.CharField(max_length=20, blank=True, null=True)
    fe_percentage = models.FloatField()
    sio2_percentage = models.FloatField()

    @property
    def overload_percentage(self):
        # Рассчитываем перегруз и возвращаем в процентах
        overload = self.current_load / self.max_load
        return round(overload * 10, 1) if overload > 1 else 0

    def __str__(self):
        return self.board_number


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    volume_before_unload = models.FloatField()
    volume_after_unload = models.FloatField(blank=True, null=True)

    sio2_percentage_before = models.FloatField()
    fe_percentage_before = models.FloatField()

    sio2_percentage_after = models.FloatField(blank=True, null=True)
    fe_percentage_after = models.FloatField(blank=True, null=True)

    polygon = models.CharField(max_length=100)
