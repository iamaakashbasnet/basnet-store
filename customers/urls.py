from django.urls import path

from .views import (
    CustomerListView,
    CustomerCreateView,
    CustomerManageView,
)


urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer-create'),
    path('customer/manage/<int:pk>/',
         CustomerManageView.as_view(), name='customer-manage')
]
