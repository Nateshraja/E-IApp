from django import forms
from django.db import models

class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255)

class Installment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255)

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('amount', 'date', 'description')
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

class InstallmentForm(forms.ModelForm):
    class Meta:
        model = Installment
        fields = ('amount', 'date', 'description')
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }
