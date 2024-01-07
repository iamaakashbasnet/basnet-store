from django.shortcuts import render, redirect
from django.db import models
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    View,
    ListView,
    CreateView,
    UpdateView,
)

from .models import Customer, Transaction
from .forms import PaymentForm


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/list_customers.html'
    context_object_name = 'customers'
    ordering = 'first_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        total_customers = Customer.objects.count()
        total_credit_balance = Customer.objects.aggregate(
            total_credit_balance=models.Sum('credit_balance'))['total_credit_balance']

        context['total_credit_balance'] = total_credit_balance
        context['total_customers'] = total_customers
        return context


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = '__all__'
    template_name = "customers/create_customer.html"
    success_url = "/customers"

    def form_valid(self, form):
        messages.success(self.request, 'Customer successfully created.')
        return super().form_valid(form)


class CustomerManageView(View):
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(pk=self.kwargs.get('pk'))
        transactions = Transaction.objects.filter(
            customer=customer).order_by('-timestamp')
        context = {'customer': customer, 'transactions': transactions}
        return render(request, template_name='customers/manage_customer.html', context=context)

    def post(self, request, *args, **kwargs):
        transaction = Transaction.objects.get(
            id=request.POST.get('transaction_id'))
        customer = Customer.objects.get(pk=self.kwargs.get('pk'))
        transaction.isPaid = True
        customer.credit_balance -= transaction.amount
        transaction.save()
        customer.save()

        messages.success(
            request, f'{transaction.description}, amount of {transaction.amount} paid.')

        return redirect('customer-manage', pk=customer.pk)


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

        messages.success(self.request, 'Transaction added successfully.')

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


class CustomerPaymentView(View):
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(pk=self.kwargs.get('pk'))
        form = PaymentForm()
        context = {'customer': customer, 'form': form}
        return render(request, template_name='customers/payment_customer.html', context=context)

    def post(self, request, *args, **kwargs):
        customer = Customer.objects.get(pk=self.kwargs.get('pk'))
        transactions = Transaction.objects.filter(
            customer=customer, isPaid=False)
        form = PaymentForm(request.POST)

        if form.is_valid():
            payment_number = form.cleaned_data['payment_number']

            if customer.credit_balance == 0:
                messages.error(request,
                               'Cannot make payment. Credit balance is already 0.00')
            else:
                customer.credit_balance -= payment_number
                customer.save()

                for transaction in transactions:
                    transaction.isPaid = True
                    transaction.save()

                messages.success(
                    request, f'Payment of Rs. {payment_number} received.')

            return redirect('customer-manage', pk=customer.pk)

        context = {'customer': customer, 'form': form}
        return render(request, template_name='customers/payment_customer.html', context=context)
