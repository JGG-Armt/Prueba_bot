import os
from fastapi import FastAPI, Request
import requests

TOKEN = "8934368812:AAE7hb0dv6sDiOrtpVW3rn4HAPvUZOzuiJw"
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/"

app = FastAPI()

def send_message(chat_id, text):
    url = TELEGRAM_URL + "sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    requests.post(url, json=payload)

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            send_message(chat_id, "Bot activo. Usa /resumen o comandos básicos.")
        elif text == "/resumen":
            send_message(chat_id, "Resumen premium del mercado (placeholder).")
        elif text == "/dax":
            send_message(chat_id, "DAX — Análisis básico (placeholder).")
        elif text == "/eurusd":
            send_message(chat_id, "EUR/USD — Análisis básico (placeholder).")

    return {"ok": True}
