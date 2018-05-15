"""car_plates_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API structure')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/login/$', obtain_jwt_token, name='api-login'),
    url(r'^$', schema_view),
    # url(r'^$', TemplateView.as_view(template_name='carplates/index.html')),
    # url(r'^', include('carplates.urls')),
    url(r'^api2/postings/', include('postings.api.urls', namespace='api-postings')),
    url(r'^api3/sweets/', include('sweets.urls', namespace='api-sweets')),
]
