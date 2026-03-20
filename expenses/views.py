from django.shortcuts import render,redirect,get_object_or_404
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


def edit_expense(request, pk):
    # Safely fetch the specific expense, or show a 404 error if it doesn't exist
    expense = get_object_or_404(Expense, pk=pk)
    
    if request.method == 'POST':
        # Pass the existing expense 'instance' to the form so it knows to UPDATE, not CREATE
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense-list')
    else:
        # Pre-fill the form with the existing expense data
        form = ExpenseForm(instance=expense)
        
    context = {'form': form}
    # Notice we can reuse the EXACT same HTML template we used for adding an expense!
    return render(request, 'expenses/expense_form.html', context)

def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    
    # We require a POST request to delete, as a security measure
    if request.method == 'POST':
        expense.delete()
        return redirect('expense-list')
        
    context = {'expense': expense}
    return render(request, 'expenses/expense_confirm_delete.html', context)
