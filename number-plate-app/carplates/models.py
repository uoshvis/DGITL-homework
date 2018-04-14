from django.db import models


class CarPlate(models.Model):
    plate_number = models.CharField(max_length=6, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.plate_number
