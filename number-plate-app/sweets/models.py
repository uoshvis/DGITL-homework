from django.db import models
from rest_framework.reverse import reverse as api_reverse


class SweetsData(models.Model):
    name = models.CharField(max_length=100)
    kcal_100 = models.FloatField()
    fat_100 = models.FloatField()
    carbohydrate_100 = models.FloatField()
    protein_100 = models.FloatField()
    sugar_100 = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def get_api_url(self, request=None):
        return api_reverse(
            'api-sweets:sweet-rud',
            kwargs={'pk': self.pk},
            request=request
        )
