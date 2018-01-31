# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.hashers import (check_password, is_password_usable, make_password)
from collections import OrderedDict

from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import (
    UNUSABLE_PASSWORD_PREFIX, identify_hasher,
)
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.forms.utils import flatatt
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.html import format_html, format_html_join
from django.utils.http import urlsafe_base64_encode
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _


# Create your models here. see docs.djangoproject.com/en/2.0/topics/db/models/
#each atribute files maps to a database column 
#The name of the table is myapp_Mode, this is derived by some model metadata but can be overridden
#an id field is added automatically to the table but this can be over writted
#name will be the databases column name
class Profiles(models.Model):
	name = models.CharField(max_length=50, unique=True, blank=True, help_text="What is Your Name ", error_messages={ 'unique': ("A user with that username already exists.")})
	milk = models.CharField(max_length=50, blank=True, help_text="Do you want Milk (Yes or No)")
	sugar = models.CharField(max_length=50, blank=True, help_text="Do you want sugar (Yes or No)")
	run = models.IntegerField(help_text="Please Enter a Number", blank=True)
	
	def set_password(self, raw_password):
		self.password = make_password(raw_password)

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch':_("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = Profiles
       
        fields = ("name", "password1", "password2", "milk","sugar","run")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
