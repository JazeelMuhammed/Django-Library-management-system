from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Multiuser, Booklist


class CreateMultiuserForm(UserCreationForm):
    class Meta:
        model = Multiuser
        fields = UserCreationForm.Meta.fields + ('email','phone')

class bookform(forms.ModelForm):
    class Meta:
        model = Booklist
        fields = '__all__'