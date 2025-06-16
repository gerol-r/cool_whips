# main_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm 
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from .models import Car
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required

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

def car_lot(request):
    cars = Car.objects.all()
    return render(request, 'car_lot.html', {'cars': cars})

@login_required
def garage(request):
    # This filters on the owner field to only include cars owned by the current user
    purchased_cars = Car.objects.filter(owner=request.user)
    return render(request, 'garage.html', {'cars': purchased_cars})

@login_required
def purchase_car(request, car_id):
    car = get_object_or_404(Car, id=car_id, owner__isnull=True, is_hidden=False)
    if request.user.coins >= car.cost:
        # Deduct coin balance from the user
        request.user.coins -= car.cost
        request.user.save()

        # Set the car details to assign it to the user
        car.owner = request.user
        car.purchase_price = car.cost
        car.acquired_at = timezone.now()
        car.acquisition_method = "purchase"
        car.save()
    return redirect('garage')

@login_required
def sell_car(request, car_id):
    car = get_object_or_404(Car, id=car_id, owner=request.user)
    sell_value = car.depreciated_value()
    request.user.coins += sell_value
    request.user.save()

    # Reset car data so it returns to the lot.
    car.owner = None
    car.purchase_price = None
    car.acquired_at = None
    car.acquisition_method = None
    car.save()
    return redirect('garage')