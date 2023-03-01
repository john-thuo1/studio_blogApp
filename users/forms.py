from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
# The forms.py is used to create new additional fields in the registration page. It inherits from the UserCreationForm

class UserRegistrationForm(UserCreationForm):
    # email = forms.EmailField(required = True)
    # Default is true, So you can leave it blank
    email = forms.EmailField(required =True)
    
    # Class Meta provides a nested namespace for configurations and keeps the configurations in one place.
    # In other words, it is the inner class of your model class. 
    # Meta is basically used to change the behavior of your model fields like changing order options,verbose_name, and a lot of other options. 
    # It's completely optional to add a Meta class to your model
    class Meta:
        model = User
        # These are the fields that will be displayed to the user while registering. 
        fields = ['username','email' ,'password1','password2',]
        
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']
   
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        

        
        
        

        