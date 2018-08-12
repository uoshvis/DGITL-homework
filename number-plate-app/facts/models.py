from django.db import models


class Fact(models.Model):
    fact = models.CharField(max_length=400)
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return str(self.fact)
