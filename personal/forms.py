# personal/forms.py
from django import forms
from .models import Contact

PRODUCT_CHOICES = [
    ('product1', '2007 Mlilo album with 10 hit songs'),
    ('product2', '2007 Mlilo DVD album'),
    ('product3','Tsa-Lapeng ft Dj Black Coffee'),
    ('product4','Tsa-Lapeng hit live show DVD'),
    ('product5','Makoti- album of the year 2010'),
    ('product6','Soldier - Collection ft Amanda Black'),
    ('product7','Matjhabeng - 16 hits full album'),
    ('product8','Hlasela - Platinum hit songs'),
    ]

class ContactForm(forms.ModelForm):
    product = forms.ChoiceField(choices=PRODUCT_CHOICES) # Add this
    class Meta:
        model = Contact
        fields = ['name', 'lastname', 'email', 'address', 'product', 'payment_slip']
