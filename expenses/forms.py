from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        # We tell Django exactly which fields we want the user to fill out.
        # Notice we left out 'created_at' because Django handles that automatically!
        fields = ['title', 'amount', 'category', 'date']