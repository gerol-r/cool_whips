# main_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm 
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
User = get_user_model()


# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
# def home(request):
#     return render(request, 'home.html')
class Home(LoginView):
    template_name = 'home.html'


#User signup function
def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = CustomUserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)