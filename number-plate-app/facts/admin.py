from django.contrib import admin

# Register your models here.
from facts.models import Fact

admin.site.register(Fact)
