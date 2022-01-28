from django.forms import ModelForm
from .models import BudgetData


class AddItem(ModelForm):
    class Meta:
        model = BudgetData
        fields = ["category", "cost"]
        help_texts = {
            "category": ("Choose a category."),
            "cost": ("Please add the exact cost."),
        }