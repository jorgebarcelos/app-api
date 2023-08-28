from ninja import NinjaAPI, ModelSchema
from .models import Customer


api = NinjaAPI()


class CustomerSchema(ModelSchema):
    class Config:
        model = Customer
        model_fields = '__all__'


@api.get('/home')
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


@api.post('customer', response=CustomerSchema)
def post_customer(request, customer: CustomerSchema):
    payload = customer.dict()
    customer = Customer(**payload)
    customer.save()
    return customer