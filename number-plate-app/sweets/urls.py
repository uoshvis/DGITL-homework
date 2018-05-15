from django.conf.urls import url

from .views import SweetsDataAPIView, SweetsDataRudView

urlpatterns = [
    url(r'^$', SweetsDataAPIView.as_view(), name='sweet-listcreate'),
    url(r'^(?P<pk>\d+)/$', SweetsDataRudView.as_view(), name='sweet-rud')
]
