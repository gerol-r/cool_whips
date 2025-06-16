from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('lot/', views.car_lot, name='car_lot'),
    path('garage/', views.garage, name='garage'),
    path('purchase/<int:car_id>/', views.purchase_car, name='purchase_car'),
    path('sell/<int:car_id>/', views.sell_car, name='sell_car'),
]

