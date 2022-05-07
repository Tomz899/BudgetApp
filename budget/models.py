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
    income = models.FloatField(default=0)
