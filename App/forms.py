from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import PersonaTest

class PersonaTestCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = PersonaTest
        fields = ('usname', 'email')

class PersonaTestChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = PersonaTest
        fields = ('usname', 'email')

# honestamente no entiendo exactamente que hacen, en la referencia no dice
# explicitamente para que sirven. solo puedo implicar que hacen.