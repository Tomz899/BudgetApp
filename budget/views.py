from django.shortcuts import render
from .models import BudgetData
from django.db.models import Sum
from django.contrib.auth.decorators import login_required


@login_required
def budget(request):
    expense_items = BudgetData.objects.filter(user_expense=request.user).order_by(
        "-date_added"
    )

    total_cost = BudgetData.objects.filter(user_expense=request.user).aggregate(
        Sum("cost")
    )

    return render(
        request,
        "budget/budget.html",
        context={
            "user": request.user,
            "expense_items": expense_items,
            "total_cost": total_cost,
        },
    )
