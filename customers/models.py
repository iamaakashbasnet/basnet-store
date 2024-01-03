from django.db import models
from django.contrib.auth import get_user_model


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    credit_balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}\'s credit balance - Rs.{self.credit_balance}'


class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.first_name} {self.customer.last_name} - Rs.{self.amount}"
