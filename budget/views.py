from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import BudgetData
from .forms import AddItem


@login_required
def budget(request):
    expense_items = BudgetData.objects.filter(user_expense=request.user).order_by(
        "-date_added"
    )

    total_cost = BudgetData.objects.filter(user_expense=request.user).aggregate(
        Sum("cost")
    )

    # add item{category, cost} form
    form = AddItem(request.POST)
    form = AddItem(
        use_required_attribute=False
    )  # this get rid of this field is required text
    if form.is_valid():
        form = form.save(commit=False)
        form.user_expense = request.user
        form.date_added = timezone.now()
        form.save()
        messages.success(request, ("Item Added!"))
        return HttpResponseRedirect(reverse("budget"))
    else:
        return render(
            request,
            "budget/budget.html",
            context={
                "user": request.user,
                "expense_items": expense_items,
                "total_cost": total_cost,
                "form": form,
            },
        )


def delete_item(request, user_id):
    item = BudgetData.objects.get(id=user_id)
    item.delete()
    messages.success(request, ("Item Deleted!"))
    return redirect("budget")
