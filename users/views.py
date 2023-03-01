from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# flash messages is used to display a one time alert to the form template that the data has been received
# Other messages methods include messages.info, messages.debug, messages.warning, messages.success
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, ProfileUpdateForm, UserUpdateForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        # Create a form that has request.POST
        form = UserRegistrationForm(request.POST)
        # Check if the data submitted in the form is valid
        
        if form.is_valid():
            # Save the user information
            form.save()
            # username = form.cleaned_data.get('username')            
            username = form.cleaned_data['username']
            messages.success(request, f'Your Account has been created!{username}, You are now able to log in')
            # Once signed up, redirect user to blog homepage
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


#User should be logged in before they view the profile. Use django decorators
@login_required   
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your Account has been updated')
            return redirect('profile')       
     
    else: 
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)  
    
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    
    return render(request, 'users/profile.html', context)


