from django.urls import path
from .views import ScheduleCreateView, ScheduleListView, ScheduleDetailView


urlpatterns = [
    path("schedules/<uuid:property_id>/", ScheduleCreateView.as_view()),
    path("schedules/detail/<uuid:schedule_id>/", ScheduleDetailView.as_view()),
    path("schedules/", ScheduleListView.as_view()),
]
