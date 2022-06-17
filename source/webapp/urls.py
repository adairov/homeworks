from django.urls import path
from webapp.views import calculate_view

urlpatterns = [
    path("", calculate_view),
]