from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# ------------------------sign up form-------------------------#
# The sign up form is already pre-made in the Django we add this function to modify it
class SignUpForm(UserCreationForm):
    Code = forms.CharField(max_length=4, required=False,
                           help_text='Required for admin only (1234)')  # add field for code
    ID = forms.CharField(max_length=14, required=True, help_text='Enter your ID Number')  # add field for id

    class Meta:  # to organize form fields
        model = User
        fields = ('username', 'password1', 'password2', 'Code', 'ID')
