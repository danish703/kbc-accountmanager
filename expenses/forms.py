from .models import Expenses,ExpensesCategory
from django import forms
class ExpensesCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpensesCategory
        fields ='__all__'


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields ='__all__'