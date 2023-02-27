from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Account


class UserRegisterForm(UserCreationForm):
    phone_number = forms.CharField(label='phone number', widget=forms.TextInput(
        attrs={'placeholder': ' for notification'}))

    class Meta:
        model = Account
        fields = ('phone_number', 'username', 'first_name',
                  'last_name', 'password1', 'password2')

    def clean(self):
        super(UserRegisterForm, self).clean()
        phone_number = self.cleaned_data.get('phone_number')
        if not (phone_number.isdigit() and len(phone_number) == 11 and phone_number[0:2] == '09'):
            self._errors['phone_number'] = self.error_class(
                ['phone number format is invalid'])
        return self.cleaned_data
