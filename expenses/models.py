from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Expense(models.Model):
    # The categories a user can choose from
    CATEGORY_CHOICES = [
        ('FOOD', 'Food & Dining'),
        ('TRANSPORT', 'Transportation'),
        ('UTILITIES', 'Bills & Utilities'),
        ('ENTERTAINMENT', 'Entertainment'),
        ('OTHER', 'Other'),
    ]

    # The actual columns in our database table
    title = models.CharField(max_length=100)
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')
    date = models.DateField()
    
    # Automatically tracks when this was added to the database
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # This controls how the expense looks in the admin panel
        return f"{self.title} - ${self.amount}"
