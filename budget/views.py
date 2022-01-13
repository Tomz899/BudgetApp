from django.shortcuts import render
from .models import BudgetData


def budget(request):
    expense_items = BudgetData.objects.filter(user_expense=request.user).order_by(
        "-date_added"
    )
    return render(
        request,
        "budget/budget.html",
        context={"user": request.user, "expense_items": expense_items},
    )
