from payloads.schemas.AddressSchema import addressRequest
from repositories import AddressRepo

def get_all_address_service():
    return AddressRepo.get_all_address()

def add_new_address_service(req: addressRequest):
    return AddressRepo.create_new_address(req)

def update_address_service(id: int, req: addressRequest):
    return AddressRepo.update_address(id, req)

def delete_address_service(id: int):
    return AddressRepo.delete_address(id)