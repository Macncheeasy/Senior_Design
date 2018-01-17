# -*- coding: utf-8 -*-
#This is essentially the controller of the application which is responsible for 
#~ making sense of requests and producing the appropriate output
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from myapp.models import  UserCreationForm,  Profiles
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
#~ from django.contrib.auth.forms import UserCreationForm
#~ from myapp.forms import SignUpForm
#~ from django.http import HttpResponseRedirect
from django import forms
from rest_framework import viewsets
from django.template import RequestContext
from django.template.response import TemplateResponse
from myapp.serializers import ProfilesSerializer
from django.contrib.auth.decorators import login_required
from django.db import transaction
import requests #this is used to ping a website or portal for information
import json

# Create your views here.
#Modelview sets extends the Generic APIView and provides actions
#.list() .retrieve() .create() .update() .partial_update() and .destroy()

class ProfilesViewSet(viewsets.ModelViewSet):
    #used to return objects from the view, this essentially gets the information put on Mode
    queryset = Profiles.objects.all()
        #used for validating and deserializing input
    serializer_class = ProfilesSerializer
    
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			#~ Once it reaches hear the user is created
			form.save()
			#These  pull the username and password from this form to be used
			#To authenticate the userm if the username and password match, the 
			#user is then logged in with function login()
			username = form.cleaned_data.get('name')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/home/')
	else:
		form = UserCreationForm()
	return render(request, 'register.html', {'form': form})


def home(request):
    #Not sure if i needed this stuff, lou included it
    #~ run = ''
    #~ currentmode = 'auto'
    #~ currentstate = 'off'
    
#if on is put in the field, within the Posted Data , this calls from the
#index.html forum  submission
    if 'run' in request.POST:
        
        values = {"run": 1}
        
        #This puts the data at the location state/1/ and the information
        #placed here is the values, 'on' and is authorized by the user        
        r = requests.put('http://127.0.0.1:8000/profiles/1/',
                        data=values, auth=('pi', 'Letsgorams1!'))
        result = r.text
        output = json.loads(result)
        out = output['run']
    
    
    if 'yes milk' in request.POST:
        values = {"milk": "yes"}
        
        #This puts the data at the location state/1/ and the information
        #placed here is the values, 'on' and is authorized by the user        
        r = requests.put('http://127.0.0.1:8000/profiles/1/',
                        data=values, auth=('pi', 'Letsgorams1!'))
        result = r.text
        output = json.loads(result)
        out = output['milk']
    if 'no milk' in request.POST:
        values = {"milk": "no"}
        
        #This puts the data at the location state/1/ and the information
        #placed here is the values, 'on' and is authorized by the user        
        r = requests.put('http://127.0.0.1:8000/profiles/1/',
                        data=values, auth=('pi', 'Letsgorams1!'))
        result = r.text
        output = json.loads(result)
        out = output['milk']
        
    if 'yes sugar' in request.POST:
        values = {"sugar": "yes"}
        #This puts the data at the location mode/1/ and the information
        #placed here is the values, auto and is authorized by the user
        r = requests.put('http://127.0.0.1:8000/profiles/1/',
                        data=values, auth=('pi', 'Letsgorams1!'))
        result = r.text
        output = json.loads(result)
        out = output['sugar']
    if 'no sugar' in request.POST:
        values = {"sugar": "no"}
        r = requests.put('http://127.0.0.1:8000/profiles/1/',
                        data=values, auth=('pi', 'Letsgorams1!'))
        result = r.text
        output = json.loads(result)
        out = output['sugar']

    r = requests.get('http://127.0.0.1:8000/profiles/1/',
                    auth=('pi', 'Letsgorams1!'))
    result = r.text
    output = json.loads(result)
    name = output['name']
    sugarpref = output['sugar']
    milkpref = output['milk']
    currentrun = output['run']

    #~ return TemplateResponse(request, 'myapp/index.html', {'run':currentrun,
    #~ 'currentmode':currentmode, 'currentstate':currentstate})
    
	#Returns the values Analyzed #This goes to the html
    return render(request, 'index.html', {'name':name,'run':currentrun,
    'sugarpref':sugarpref, 'milkpref':milkpref})
