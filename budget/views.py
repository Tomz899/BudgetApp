from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone

from .forms import AddIncome, AddItem
from .models import BudgetData, IncomeData


@login_required
def budget(request):
    expense_items = BudgetData.objects.filter(user_expense=request.user).order_by(
        "-date_added"
    )

    # Setting up pagination per expense_items
    paginator = Paginator(expense_items, 10, 3)  # Show 10 items per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    total_cost = BudgetData.objects.filter(user_expense=request.user).aggregate(
        total_cost=Sum("cost")
    )
    total_income = IncomeData.objects.filter(user_income=request.user).aggregate(
        total_income=Sum("income")
    )
    amount_left = sum(total_income.values()) - sum(total_cost.values())

    # Instantiating the forms
    a_form = AddItem()
    b_form = AddIncome()

    if request.method == "POST" and "expense" in request.POST:
        a_form = AddItem(request.POST)
        if a_form.is_valid():
            a_form = a_form.save(commit=False)
            a_form.user_expense = request.user
            a_form.date_added = timezone.now()
            a_form.save()
            return HttpResponseRedirect(reverse("budget"))
    if request.method == "POST" and "income" in request.POST:
        b_form = AddIncome(request.POST)
        if b_form.is_valid():
            b_form = b_form.save(commit=False)
            b_form.user_income = request.user
            b_form.date_added = timezone.now()
            b_form.save()
            return HttpResponseRedirect(reverse("budget"))
        print(b_form.errors)

    return render(
        request,
        "budget/budget.html",
        context={
            "user": request.user,
            "expense_items": expense_items,
            "total_cost": total_cost,
            "total_income": total_income,
            "a_form": a_form,
            "b_form": b_form,
            "page_obj": page_obj,
            "amount_left": amount_left,
        },
    )


# def add_income(request):
#     if request.method == "POST":
#         form = AddIncome(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.user_expense = request.user
#             form.save()
#             return HttpResponseRedirect(reverse("budget"))
#     else:
#         return render(
#             request,
#             "budget/budget.html",
#             context={
#                 "user": request.user,
#                 "form": form,
#             },
#         )


def delete_item(request, user_id):
    item = BudgetData.objects.get(id=user_id)
    item.delete()
    messages.success(request, ("Item Deleted!"))
    return redirect("budget")
