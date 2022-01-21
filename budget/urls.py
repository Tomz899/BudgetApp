from django.urls import path

from . import views

urlpatterns = [
    path("budget/", views.budget, name="budget-page"),
]
