from django import forms


class PaymentForm(forms.Form):
    payment_number = forms.DecimalField(
        label='Amount', decimal_places=2)
