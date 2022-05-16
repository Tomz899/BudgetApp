from django.forms import ModelForm

from .models import BudgetData, IncomeData


class AddItem(ModelForm):
    class Meta:
        model = BudgetData
        fields = ["category", "cost"]
        help_texts = {
            "category": ("Choose a category."),
            "cost": ("Please add the exact cost."),
        }


class AddIncome(ModelForm):
    class Meta:
        model = IncomeData
        fields = ["income"]
        help_texts = {
            "income": ("Add your income."),
        }
