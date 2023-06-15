from django.shortcuts import render, get_object_or_404, redirect
from .forms import ExpenseForm, InstallmentForm
from .models import Expense, Installment


def home(request):
    return render(request, 'expenses/home.html')


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expenses:report')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

def add_installment(request):
    if request.method == 'POST':
        form = InstallmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expenses:report')
    else:
        form = InstallmentForm()
    return render(request, 'expenses/add_installment.html', {'form': form})

def generate_report(request):
    expenses = Expense.objects.all()
    installments = Installment.objects.all()
    return render(request, 'expenses/report.html', {'expenses': expenses, 'installments': installments})

def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expenses:report')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/edit_expense.html', {'form': form, 'expense': expense})

def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('expenses:report')
    return render(request, 'expenses/delete_expense.html', {'expense': expense})

def edit_installment(request, pk):
    installment = get_object_or_404(Installment, pk=pk)
    if request.method == 'POST':
        form = InstallmentForm(request.POST, instance=installment)
        if form.is_valid():
            form.save()
            return redirect('expenses:report')
    else:
        form = InstallmentForm(instance=installment)
    return render(request, 'expenses/edit_installment.html', {'form': form, 'installment': installment})

def delete_installment(request, pk):
    installment = get_object_or_404(Installment, pk=pk)
    if request.method == 'POST':
        installment.delete()
        return redirect('expenses:report')
    return render(request, 'expenses/delete_installment.html', {'installment': installment})
