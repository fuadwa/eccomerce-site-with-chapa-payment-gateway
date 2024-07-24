import time
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from getway import Payment
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello World"}

class Payit(BaseModel):
    email: str = 'test@gmail.com'
    fname: str = 'test'
    lname: str = 'test'
    amount: int = 250
    rdurl: str = 'https://www.google.com'

@app.post('/pay')
def pay(payit: Payit):
    data = Payment.pay(email=payit.email, fname=payit.fname, lname=payit.lname, amount=payit.amount, rdurl=payit.rdurl)
    return data

class Txnum(BaseModel):
    ref_num: str = ''

@app.post('/ver')
def verify(txnum: Txnum):
    ver = Payment.custom_verify(transaction_ref=txnum.ref_num)
    return ver
