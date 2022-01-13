from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class BudgetData(models.Model):
    category = models.CharField(max_length=20)
    cost = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now)
    user_expense = models.ForeignKey(User, on_delete=models.CASCADE, default="")
