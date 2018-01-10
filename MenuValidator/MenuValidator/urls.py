from django.conf.urls import url
from backendwebapp import views

urlpatterns = [
    url(r'^fetch-menus$', views.fetch_menus, name='menus'),
]
