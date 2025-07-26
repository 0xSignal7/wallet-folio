import os
from dotenv import load_dotenv
import requests
from covalent import CovalentClient

load_dotenv()

API_KEY = os.getenv("GOLDRUSH_API_KEY")
if not API_KEY:
    raise ValueError("API key not found. Check your .env file or environment variables.")

client = CovalentClient(API_KEY)



def get_token_balances(wallet_address: str, chain: str = "eth-mainnet"):
    url = f"https://api.covalenthq.com/v1/{chain}/address/{wallet_address}/balances_v2/"
    params = {"key": API_KEY}
    resp = requests.get(url, params=params)

    if resp.status_code == 200:
        return resp.json()
    else:
        return {"error": True, "message": f"HTTP {resp.status_code}: {resp.text}"}

# def get_token_balances(wallet_address: str, chain: str = "eth-mainnet"):
#     response = client.balance_service.get_token_balances_for_wallet_address(chain, wallet_address)
#
#     # DEBUG
#     print("DEBUG - response.error:", response.error)
#     print("DEBUG - response.error_message:", response.error_message)
#     print("DEBUG - response.data:", response.data)
#
#     if not response.error:
#         return response.data
#     else:
#         error_msg = response.error_message or "Unknown error from API"
#         return {"error": True, "message": error_msg}