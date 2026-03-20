from django.shortcuts import render,redirect
from .forms import ExpenseForm
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

def add_expense(request):
    # 1. If the user clicks "Submit" on the form (POST request)
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save() # Saves the new expense to the database!
            return redirect('expense-list') # Send them back to the list page
            
    # 2. If the user is just visiting the page for the first time (GET request)
    else:
        form = ExpenseForm() # Create an empty form
        
    context = {'form': form}
    return render(request, 'expenses/expense_form.html', context)
