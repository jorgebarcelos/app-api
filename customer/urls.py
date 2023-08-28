from django.urls import path
from customer.api import api


urlpatterns = [
    path('', api.urls),
]
