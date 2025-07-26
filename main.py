# main.py (ou app/main.py si tu préfères)
import uvicorn

def main():
    uvicorn.run("app.api:app", host="127.0.0.1", port=8001, reload=True)

if __name__ == "__main__":
    main()

#0x0058faedf76999c0a4a1dcc27dc78e61dd5cc0b9
#http://127.0.0.1:8001/wallet/0x0058faedf76999c0a4a1dcc27dc78e61dd5cc0b9
