from django.urls import path

from . import views

urlpatterns = [
    path("", views.budget, name="budget"),
    path("budget/", views.budget, name="budget"),
    path("delete_item/<int:user_id>", views.delete_item, name="delete-item"),
]
