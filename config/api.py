from ninja import NinjaAPI
from customer.api import router as customer_router

api = NinjaAPI()
api.add_router('customer/', customer_router)