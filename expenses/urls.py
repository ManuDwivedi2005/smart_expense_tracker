from django.urls import path
from . import views

urlpatterns = [
    # When someone goes to the base URL of this app, trigger the expense_list view
    path('', views.expense_list, name='expense-list'),
    path('add/', views.add_expense, name='add-expense'),
]