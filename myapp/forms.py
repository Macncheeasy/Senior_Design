#~ from django import forms
#~ from myapp.models import Mode
#~ from django.contrib.auth.forms import UserCreationForm
#~ from django.contrib.auth.models import User


#~ class SignUpForm(UserCreationForm):
	#~ name = forms.CharField(max_length=50, help_text="What is Your Name")
	#~ milk = forms.CharField(max_length=50, help_text="Do you want Milk")
	#~ sugar = forms.CharField(max_length=50, help_text="Do you want sugar")
	#~ run = forms.IntegerField(help_text="Please Enter a Number")
	





#~ class UserRegistrationForm(forms.Form):
    #~ username = forms.CharField(
        #~ required = True,
        #~ label = 'Username',
        #~ max_length = 32
    #~ )
    #~ email = forms.CharField(
        #~ required = True,
        #~ label = 'Email',
        #~ max_length = 32,
    #~ )
    #~ password = forms.CharField(
        #~ required = True,
        #~ label = 'Password',
        #~ max_length = 32,
        #~ widget = forms.PasswordInput()
    #~ )
