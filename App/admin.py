from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Est, PersonaTest
from .forms import PersonaTestCreationForm, PersonaTestChangeForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = PersonaTestCreationForm
    form = PersonaTestChangeForm
    model = PersonaTest
    list_display = ['email', 'usname',]


admin.site.register(PersonaTest, CustomUserAdmin)

# Por lo que entendi, de no incorporar un CustomUserAdmin, Django se cae
# al hacer migraciones. 