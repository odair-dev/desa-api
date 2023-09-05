from django.urls import path
from .views import AccountView, AccountDetail
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("accounts/", AccountView.as_view()),
    path("accounts/<uuid:account_id>/", AccountDetail.as_view()),
    path("login/", jwt_views.TokenObtainPairView.as_view()),
]
