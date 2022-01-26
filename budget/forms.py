from django.forms import ModelForm
from .models import BudgetData


class AddItem(ModelForm):
    class Meta:
        model = BudgetData
        fields = ["category", "cost"]
