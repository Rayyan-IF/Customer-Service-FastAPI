from payloads.schemas.AddressSchema import addressRequest
from entities.AddressEntity import addressModel
from configs.database import connect_db
from fastapi import HTTPException

def get_all_address():
    db = connect_db()
    try:
        address = db.query(addressModel).all()
        return {"address": address}
    except Exception as e:
         raise HTTPException(status_code=500, detail=f"Gagal mengambil data leads. Error: {str(e)}")

def create_new_address(req: addressRequest):
    db = connect_db()
    try:
       _new_data = addressModel()
       _new_data.customer_id = req.customer_id
       _new_data.address = req.address
       _new_data.district = req.district
       _new_data.city = req.city
       _new_data.province = req.province
       _new_data.postal_code = req.postal_code
       db.add(_new_data)
       db.commit()
       db.refresh(_new_data)
       return {"Created":_new_data}
    except Exception as err:
       db.rollback()
       return None, err
    
def update_address(id: int, req: addressRequest):
    db = connect_db()
    try:
        existing_address = db.query(addressModel).filter(addressModel.id == id).first()
        if existing_address:
            existing_address.address = req.address
            existing_address.district = req.district
            existing_address.city = req.city
            existing_address.province = req.province
            existing_address.postal_code = req.postal_code

            db.commit()
            db.refresh(existing_address)

            return {"Updated": existing_address}
        else:
            raise HTTPException(status_code=404, detail="Customer not found")

    except Exception as err:
        db.rollback()
        return None, err
    
def delete_address(id: int):
    db = connect_db()
    try:
        existing_address = db.query(addressModel).filter(addressModel.id == id).first()

        if existing_address:
            db.delete(existing_address)
            db.commit()

            return {"Deleted": existing_address}
        else:
            raise HTTPException(status_code=404, detail="Customer not found")

    except Exception as err:
        db.rollback()
        return None, err