from django.urls import path
from .views import PropertyView


urlpatterns = [
    path("properties/", PropertyView.as_view()),
]
