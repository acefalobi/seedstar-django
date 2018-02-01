import re

from django import forms
from django.core.exceptions import ObjectDoesNotExist

from profile_app.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']

        if not re.search(r'^[^@]+@[^@]+\.[^@]+', email):
            raise forms.ValidationError('Email is invalid.')

        try:
            Profile.objects.get(email=email)
            Profile.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError('Email has already been added.')
