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