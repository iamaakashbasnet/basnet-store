from django.views.generic import ListView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

from .models import Customer, Transaction


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/list_customers.html'
    context_object_name = 'customers'
    ordering = 'first_name'
