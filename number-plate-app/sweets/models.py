from django.db import models
from rest_framework.reverse import reverse as api_reverse


class SweetsData(models.Model):
    name = models.CharField(max_length=30)
    weight_grams = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    kcal = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def get_api_url(self, request=None):
        return api_reverse(
            'api-sweets:sweet-rud',
            kwargs={'pk': self.pk},
            request=request
        )
