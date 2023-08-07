from fastapi.middleware.cors import CORSMiddleware
from controllers.CustomerController import router1
from controllers.AddressController import router2
from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router1)
app.include_router(router2)