from django.urls import path
from customer.views import *

urlpatterns = [
    path('', customer_list, name='customer_list'),
]
