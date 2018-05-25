from django.conf.urls import url
from .views import (
    FactsAPIView,
    FactsRudView
)


urlpatterns = [
    url(r'^$', FactsAPIView.as_view(), name='facts-listcreate'),
    url(r'^(?P<pk>\d+)/$', FactsRudView.as_view(), name='facts-rud'),
]
