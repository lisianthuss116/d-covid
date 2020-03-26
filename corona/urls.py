from django.urls import path
from .views import *

urlpatterns = [
    # main page
    path('', main, name='main'),
    # datas-card page
    path('as_card/', as_card, name='as_card'),
]
