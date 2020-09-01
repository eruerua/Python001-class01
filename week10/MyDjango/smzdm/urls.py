from django.urls import path
from . import views


urlpatterns = [
    path('', views.phones_short),
    path('search/',views.search,name='search')
]