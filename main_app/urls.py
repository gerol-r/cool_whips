from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),
]

