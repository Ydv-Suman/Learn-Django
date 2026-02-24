from django.urls import path
from . import views

urlpatterns = [
    path("", views.daily_track_list, name="list-daily-track"),
    path("create/", views.create_daily_track, name="create-daily-track"),
    path("<int:id>/update/", views.update_daily_track, name="update-daily-track"),
    path("<int:id>/delete/", views.delete_daily_track, name="delete-daily-track")
]
