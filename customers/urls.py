from django.urls import path

from .views import (
    CustomerListView,
    CustomerCreateView,
    CustomerManageView,
    TransactionCreateView,
    CustomerEditView,
    CustomerPaymentView
)


urlpatterns = [
    path('', CustomerListView.as_view(), name='customer-list'),
    path('create/', CustomerCreateView.as_view(), name='customer-create'),
    path('edit/<int:pk>/', CustomerEditView.as_view(), name='customer-edit'),

    path('manage/<int:pk>/',
         CustomerManageView.as_view(), name='customer-manage'),
    path('transaction/<int:pk>/create/', TransactionCreateView.as_view(),
         name='transaction-create'),
    path('payment/<int:pk>/',
         CustomerPaymentView.as_view(), name='customer-payment')
]
