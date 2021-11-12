from django.db import models

class UserAccount(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class BudgetData(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    user_budget = models.IntegerField()
    expenses = models.IntegerField()
    category = models.CharField(max_length=15)
