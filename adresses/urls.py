from django.urls import path
from .views import AddressView, AddressDetailView


urlpatterns = [
    path("adresses/", AddressView.as_view()),
    path("adresses/<uuid:address_id>/", AddressDetailView.as_view()),
]
