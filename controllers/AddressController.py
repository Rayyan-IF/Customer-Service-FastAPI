from payloads.schemas.AddressSchema import addressRequest
from services import AddressService
from fastapi import APIRouter

router2 = APIRouter()

#Get all address
@router2.get("/address")
async def get_addresses():
    return AddressService.get_all_address_service()

#Create new address
@router2.post("/address")
async def post_new_address(req: addressRequest):
    return AddressService.add_new_address_service(req)

# Update address
@router2.put("/address/{id}")
async def update_address_data(id: int, req: addressRequest):
    return AddressService.update_address_service(id, req)

# Delete address
@router2.delete("/address/{id}")
async def delete_address_data(id: int):
    return AddressService.delete_address_service(id)