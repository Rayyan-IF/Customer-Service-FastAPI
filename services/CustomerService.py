from payloads.schemas.CustomerSchema import customerRequest
from repositories import CustomerRepo

def get_all_customers_service():
    return CustomerRepo.get_all_customers()

def get_customer_id_service(id: int):
    return CustomerRepo.get_customer_byId(id)

def add_new_customer_service(req: customerRequest):
    return CustomerRepo.create_new_customer(req)

def update_customer_service(id: int, req: customerRequest):
    return CustomerRepo.update_customer(id, req)

def delete_customer_service(id: int):
    return CustomerRepo.delete_customer(id)