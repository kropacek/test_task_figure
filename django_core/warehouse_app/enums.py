from django.db import models


class BoardNumberChoices(models.TextChoices):
    BOARD_101 = '101', '101'
    BOARD_102 = '102', '102'
    BOARD_K103 = 'K103', 'K103'


class ModelChoices(models.TextChoices):
    BELAZ = 'БЕЛАЗ', 'БЕЛАЗ'
    KOMATSU = 'Komatsu', 'Komatsu'
