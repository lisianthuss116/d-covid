from django.urls import path
from .views import *

urlpatterns = [
    # main page
    path('/', main, name='main'),
]
