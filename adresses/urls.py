from django.urls import path
from .views import AddressView


urlpatterns = [
    path("adresses/", AddressView.as_view()),
]
