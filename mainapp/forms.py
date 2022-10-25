from django import forms
from .models import Kiyim


# Create your forms here.
class KiyimForm(forms.ModelForm):

    class Meta:
        model = Kiyim
        fields = ('nomi','turi','ulcham','narxi')
