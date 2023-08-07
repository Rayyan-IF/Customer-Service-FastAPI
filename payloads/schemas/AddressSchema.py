from pydantic import BaseModel

class addressRequest(BaseModel):
    customer_id:int
    address:str
    district : str
    city : str
    province: str
    postal_code : str