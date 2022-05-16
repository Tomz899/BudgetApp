from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class BudgetData(models.Model):
    SPOZYWCZE = "Spożywcze"
    CHEMIA = "Chemia"
    RACHUNKI = "Rachunki"
    ALKOHOL = "Alkohol"
    GRY = "Gry"

    CATEGORY_CHOICES = [
        (SPOZYWCZE, "Spożywcze"),
        (CHEMIA, "Chemia"),
        (RACHUNKI, "Rachunki"),
        (ALKOHOL, "Alkohol"),
        (GRY, "Gry"),
    ]
    category = models.TextField(choices=CATEGORY_CHOICES, default=SPOZYWCZE)
    cost = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now)
    user_expense = models.ForeignKey(User, on_delete=models.CASCADE, default="")

    def __str__(self):
        return f"{self.category} ID: {self.id}"


class IncomeData(models.Model):
    user_income = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    date_added = models.DateTimeField(default=timezone.now)
    income = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user_income} ID: {self.id}"
