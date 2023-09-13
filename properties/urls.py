from django.urls import path
from .views import PropertyView, PropertyDetailView


urlpatterns = [
    path("properties/", PropertyView.as_view()),
    path("properties/<uuid:property_id>/", PropertyDetailView.as_view()),
]
