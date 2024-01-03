from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    View,
    ListView,
    CreateView,
)

from .models import Customer, Transaction


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/list_customers.html'
    context_object_name = 'customers'
    ordering = 'first_name'


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = '__all__'
    template_name = "customers/create_customer.html"
    success_url = "/customers"


class CustomerManageView(View):
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(pk=self.kwargs.get('pk'))
        transactions = Transaction.objects.filter(customer=customer)
        context = {'customer': customer, 'transactions': transactions}
        return render(request, template_name='customers/manage_customer.html', context=context)
