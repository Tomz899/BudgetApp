from django.urls import path

from . import views

urlpatterns = [
    path("", views.budget, name="budget"),
    path("delete_item/<item_id>", views.delete_item, name="delete-item"),
]
