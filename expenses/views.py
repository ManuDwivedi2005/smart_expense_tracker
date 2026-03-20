from django.shortcuts import render
from .models import Expense

def expense_list(request):
    # Fetch all expenses from the database, ordered by the newest date first
    all_expenses = Expense.objects.all().order_by('-date')
    
    # Package the data into a dictionary called 'context'
    context = {
        'expenses': all_expenses
    }
    
    # Send the request, the template name, and the data to be rendered
    return render(request, 'expenses/expense_list.html', context)
