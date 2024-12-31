from django.contrib.auth.hashers import make_password
from django import forms
from .models import TennisClubMember

from django import forms
from .models import TennisClubMember

class TennisClubMemberRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = TennisClubMember
        fields = [
            'first_name', 'last_name', 'email', 'phone_number',
            'date_of_birth', 'address', 'membership_type',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if TennisClubMember.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if TennisClubMember.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already registered.")
        return email

    def save(self, commit=True):
        # Get the instance without saving yet
        instance = super().save(commit=False)
        # Hash the password
        instance.password = make_password(self.cleaned_data['password'])
        if commit:
            instance.save()
        return instance


class TennisClubMemberLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class TennisClubMemberProfileForm(forms.ModelForm):
    class Meta:
        model = TennisClubMember
        fields = [
            'first_name', 'last_name', 'email', 'phone_number',
            'address', 'date_of_birth', 'membership_type'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }