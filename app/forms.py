from django import forms
from app.models import Pizza, Client, Order

class PizzaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PizzaForm, self).__init__(*args, **kwargs)
        # Estableciendo dinámicamente las opciones de 'choices' para 'flavor'
        self.fields['flavor'].widget = forms.Select(choices=Pizza.FLAVOR_CHOICES, attrs={'class': 'browser-default'})
    class Meta:
        model = Pizza
        fields = ['name', 'flavor']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'pizza',]
        widgets = {
            'client': forms.Select(attrs={'class': 'browser-default'}),
            'pizza': forms.Select(attrs={'class': 'browser-default'}),
        }
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        # Asegurándose de que el campo 'pizza' en el formulario use PizzaForm para renderizar el campo 'flavor'
        self.fields['pizza'].queryset = Pizza.objects.all()