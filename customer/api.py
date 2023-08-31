from ninja import ModelSchema, Router
from typing import List
from .models import Customer


router = Router()


class CustomerSchema(ModelSchema):
    class Config:
        model = Customer
        model_fields = "__all__"


@router.get('customer')
def home(request):
    customers = Customer.objects.all()
    response = [
        {
            'id': customer.id, 
            'name': customer.name,  
            'cnpj': customer.cnpj, 
            'description': customer.description
        } 
        for customer in customers
    ]
    return response


@router.post('customer', response=CustomerSchema)
def post_customer(request, customer: CustomerSchema):
    payload = Customer.objects.create(**customer.dict())
    return payload