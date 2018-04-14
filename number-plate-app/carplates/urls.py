from django.conf.urls import include, url
from rest_framework import routers
from carplates.views import CarPlatesViewSet


router = routers.DefaultRouter()
router.register(r'carplates', CarPlatesViewSet, base_name='position')

urlpatterns = [
    url(r'^api/', include(router.urls, namespace='api'))
]
