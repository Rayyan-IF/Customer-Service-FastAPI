from payloads.schemas.CustomerSchema import customerRequest
from entities.CustomerEntity import customerModel
from configs.database import connect_db
from fastapi import HTTPException

def get_all_customers():
    db = connect_db()
    try:
        customer = db.query(customerModel).all()
        return {"customers": customer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gagal mengambil data leads. Error: {str(e)}")
    
def get_customer_byId(id: int):
    db = connect_db()
    try:
        customer = db.query(customerModel).filter(customerModel.id == id).first()
        return {"customer": customer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gagal mengambil data leads. Error: {str(e)}")

def create_new_customer(req: customerRequest):
   db = connect_db()
   try:
       _new_data = customerModel()
       _new_data.title = req.title
       _new_data.name = req.name
       _new_data.gender = req.gender
       _new_data.phone_number = req.phone_number
       _new_data.email = req.email
       _new_data.image = req.image
       db.add(_new_data)
       db.commit()
       db.refresh(_new_data)
       return {"Created":_new_data}
   except Exception as err:
       db.rollback()
       return None, err

def update_customer(id: int, req: customerRequest):
    db = connect_db()
    try:
        existing_customer = db.query(customerModel).filter(customerModel.id == id).first()

        if existing_customer:
            existing_customer.title = req.title
            existing_customer.name = req.name
            existing_customer.gender = req.gender
            existing_customer.phone_number = req.phone_number
            existing_customer.email = req.email
            existing_customer.image = req.image

            db.commit()
            db.refresh(existing_customer)

            return {"Updated": existing_customer}
        else:
            raise HTTPException(status_code=404, detail="Customer not found")

    except Exception as err:
        db.rollback()
        return None, err
    
def delete_customer(id: int):
    db = connect_db()
    try:
        existing_customer = db.query(customerModel).filter(customerModel.id == id).first()

        if existing_customer:
            db.delete(existing_customer)
            db.commit()

            return {"Deleted": existing_customer}
        else:
            raise HTTPException(status_code=404, detail="Customer not found")

    except Exception as err:
        db.rollback()
        return None, err