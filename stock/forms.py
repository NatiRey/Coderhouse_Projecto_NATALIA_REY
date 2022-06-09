from django import forms


class StockForm(forms.Form):
    piece = forms.CharField(max_length=40, min_length=3, label='Nombre de la Entrega')
    add_date = forms.DateField(
        label='Created on',
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
    )
    is_delivered = forms.BooleanField(label='Available', required=False)
