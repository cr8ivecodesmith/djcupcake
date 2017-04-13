from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^$', views.cupcake_list, name='cupcake_list'),
]
