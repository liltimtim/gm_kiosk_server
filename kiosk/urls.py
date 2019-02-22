from django.urls import path
from .views import KioskList

urlpatterns = [
    path('', KioskList.as_view())
]