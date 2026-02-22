from django.urls import path
from . import views

urlpatterns = [
    path("", views.gallery_list, name="gallery-list"),
    path("add/", views.add_image_page, name="add-image-page"),
    path("upload-image/", views.add_image, name="upload-image"),
    path("<slug:slug>/", views.image_detail, name="image-detail"),
    path("<slug:slug>/delete/", views.delete_image, name="delete-image"),
]