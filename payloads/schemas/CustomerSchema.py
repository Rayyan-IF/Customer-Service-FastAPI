from pydantic import BaseModel

class customerRequest(BaseModel):
    title : str
    name: str
    gender : str
    phone_number : str
    image : str
    email : str