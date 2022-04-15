from cmath import polar
from unicodedata import name
from django.urls import path
from .views import areachart, bubblechart, columnchart, dpchart, home, barchart, piechart, polarchart, radarchart

urlpatterns = [
    path('', home, name='homepage'),
    path('area/', areachart, name = 'area'),
    path('bar/', barchart, name = 'bar'),
    path('bubble/', bubblechart, name = 'bubble'),
    path('dp/', dpchart, name = 'dp'),
    path('pie/', piechart, name = 'pie'),
    path('column/',columnchart,name = 'column'),
    path('polar/', polarchart, name = 'polar'),
    path('radar/', radarchart, name = 'radar')
]
