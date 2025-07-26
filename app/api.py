from fastapi import FastAPI
from app.services.covalent_service import get_token_balances
app = FastAPI()

@app.get("/wallet/{address}")
def wallet_overview(address: str):
    return get_token_balances(address)
