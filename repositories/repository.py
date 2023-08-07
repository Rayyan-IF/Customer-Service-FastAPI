from entities.LeadEntity import customerModel
from configs.database import connect_db
from fastapi import HTTPException


def getAll_customers():
    db = connect_db()
    try:
        customer = db.query(customerModel).all()
        return {"customers": customer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gagal mengambil data leads. Error: {str(e)}")