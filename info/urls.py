# info

from django.urls import path
from .views import main, check

urlpatterns = [
    path('', main),
    path('check/', check),
]
