from django.forms import ModelForm 
from .models import Person 

class ClientForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'photo']