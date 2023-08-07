from payloads.schemas.CustomerSchema import customerRequest
from services import CustomerService
from fastapi import APIRouter

router1 = APIRouter()

#Get all customers
@router1.get("/customers")
async def get_customers():
    return CustomerService.get_all_customers_service()

#Get customer by id
@router1.get("/customer/{id}")
async def get_customers_byId(id: int):
    return CustomerService.get_customer_id_service(id)

#Create new customer
@router1.post("/customer")
async def post_new_customer(req: customerRequest):
    return CustomerService.add_new_customer_service(req)

# Update customer
@router1.put("/customer/{id}")
async def update_customer_data(id: int, req: customerRequest):
    return CustomerService.update_customer_service(id, req)

#Delete customer
@router1.delete("/customer/{id}")
async def delete_customer_data(id: int):
    return CustomerService.delete_customer_service(id)