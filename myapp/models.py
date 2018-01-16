# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here. see docs.djangoproject.com/en/2.0/topics/db/models/
#each atribute files maps to a database column 
#The name of the table is myapp_Mode, this is derived by some model metadata but can be overridden
#an id field is added automatically to the table but this can be over writted
#name will be the databases column name
class Mode(models.Model):
	name = models.CharField(max_length=50, help_text="What is Your Name", default='Austin')
	milk = models.CharField(max_length=50, help_text="Do you want Milk", default='No')
	sugar = models.CharField(max_length=50, help_text="Do you want sugar", default='Yes')
	run = models.IntegerField(help_text="Please Enter a Number", default=1)

