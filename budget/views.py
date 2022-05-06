from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone

from .forms import AddItem
from .models import BudgetData


@login_required
def budget(request):
    expense_items = BudgetData.objects.filter(user_expense=request.user).order_by(
        "-date_added"
    )

    # Setting up pagination per expense_items
    paginator = Paginator(expense_items, 10)  # Show 10 items per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    total_cost = BudgetData.objects.filter(user_expense=request.user).aggregate(
        Sum("cost")
    )

    # AddItem{category, cost} form
    form = AddItem(request.POST)
    # form = AddItem(use_required_attribute=False) # ignores the field required text

    if form.is_valid():
        form = form.save(commit=False)
        form.user_expense = request.user
        form.date_added = timezone.now()
        form.save()
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
                "page_obj": page_obj,
            },
        )


def delete_item(request, user_id):
    item = BudgetData.objects.get(id=user_id)
    item.delete()
    messages.success(request, ("Item Deleted!"))
    return redirect("budget")
