from django import forms
from .models import Expense, Installment

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('amount', 'date', 'description')

class InstallmentForm(forms.ModelForm):
    class Meta:
        model = Installment
        fields = ('amount', 'date', 'description')
