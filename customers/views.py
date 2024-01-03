from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    View,
    ListView,
    CreateView,
    UpdateView,
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
        transactions = Transaction.objects.filter(
            customer=customer).order_by('-timestamp')
        context = {'customer': customer, 'transactions': transactions}
        return render(request, template_name='customers/manage_customer.html', context=context)


class TransactionCreateView(CreateView):
    model = Transaction
    fields = ['amount', 'description']
    template_name = 'customers/create_transaction.html'

    def form_valid(self, form):
        customer = Customer.objects.get(pk=self.kwargs.get('pk'))
        form.instance.customer = customer
        response = super().form_valid(form)

        customer.credit_balance += form.cleaned_data['amount']
        customer.save()

        return response

    def get_success_url(self):
        customer = self.kwargs.get('pk')
        return reverse_lazy('customer-manage', kwargs={'pk': customer})


class CustomerEditView(UpdateView):
    model = Customer
    fields = ['first_name', 'last_name']
    template_name = 'customers/edit_customer.html'

    def get_success_url(self):
        customer = self.kwargs.get('pk')
        return reverse_lazy('customer-manage', kwargs={'pk': customer})
