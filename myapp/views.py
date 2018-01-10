# -*- coding: utf-8 -*-
#This is essentially the controller of the application which is responsible for 
#~ making sense of requests and producing the appropriate output
from __future__ import unicode_literals

from django.shortcuts import render
from myapp.models import Mode, State
from rest_framework import viewsets
from django.template import RequestContext
from myapp.serializers import ModeSerializer, StateSerializer
import requests #this is used to ping a website or portal for information
import json

# Create your views here.
#Modelview sets extends the Generic APIView and provides actions
#.list() .retrieve() .create() .update() .partial_update() and .destroy()

class ModeViewSet(viewsets.ModelViewSet):
    #used to return objects from the view, this essentially gets the information put on Mode
    queryset = Mode.objects.all()
        #used for validating and deserializing input
    serializer_class = ModeSerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

def home(request):
    out = ''
    currentmode = 'auto'
    currentstate = 'off'
#if on is put in the field, within the Posted Data  
    if 'on' in request.POST:
        values = {"name": "on"}
        
        #This puts the data at the location state/1/ and the information
        #placed here is the values, 'on' and is authorized by the user        
        r = requests.put('http://127.0.0.1:8000/state/1/',
                        data=values, auth=('pi', 'Letsgorams1!'))
        result = r.text
        output = json.loads(result)
        out = output['name']
    if 'off' in request.POST:
        values = {"name": "off"}
        r = requests.put('http://127.0.0.1:8000/state/1/',
                        data=values, auth=('pi', 'Letsgorams1!'))
        result = r.text
        output = json.loads(result)
        out = output['name']
    
    
    if 'auto' in request.POST:
        values = {"name": "auto"}
        #This puts the data at the location mode/1/ and the information
        #placed here is the values, auto and is authorized by the user
        r = requests.put('http://127.0.0.1:8000/mode/1/',
                        data=values, auth=('pi', 'Letsgorams1!'))
        result = r.text
        output = json.loads(result)
        out = output['name']
    if 'manual' in request.POST:
        values = {"name": "manual"}
        r = requests.put('http://127.0.0.1:8000/mode/1/',
                        data=values, auth=('pi', 'Letsgorams1!'))
        result = r.text
        output = json.loads(result)
        out = output['name']

    r = requests.get('http://127.0.0.1:8000/mode/1/',
                    auth=('pi', 'Letsgorams1!'))
    result = r.text
    output = json.loads(result)
    currentmode = output['name']

    r = requests.get('http://127.0.0.1:8000/state/1/',
                    auth=('pi', 'Letsgorams1!'))
    result = r.text
    output = json.loads(result)
    currentstate = output['name']
	
	#Returns the values Analyzed 
    return render(request, 'myapp/index.html', {'name':out,
    'currentmode':currentmode, 'currentstate':currentstate})
