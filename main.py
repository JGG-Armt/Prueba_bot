import os
from fastapi import FastAPI, Request
import requests
import datetime

# ---------------------------------------------------------
# PEGA AQUÍ TU TOKEN REAL ENTRE COMILLAS
# EJEMPLO:
# TOKEN = "8934368812:AAE7hb0dv6sDiOrtpVW3rn4HAPvUZOzuiJw"
# ---------------------------------------------------------
TOKEN = "8934368812:AAE7hb0dv6sDiOrtpVW3rn4HAPvUZOzuiJw"

TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/"

app = FastAPI()

# ---------------------------
# Función para enviar mensajes
# ---------------------------
def send_message(chat_id, text):
    url = TELEGRAM_URL + "sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    requests.post(url, json=payload)

# ---------------------------
# Función para enviar gráficos (placeholder)
# ---------------------------
def send_chart(chat_id, title):
    send_message(chat_id, f"📈 Gráfico premium: <b>{title}</b>\n(placeholder)")

# ---------------------------
# Informes automáticos
# ---------------------------
def informe_0600():
    hoy = datetime.date.today().strftime("%d/%m/%Y")
    return f"""
<b>📊 Informe Premium — {hoy}</b>

<b>1. Mapa técnico</b>
• SP500: Alcista, soporte 5200
• DAX: Alcista, soporte 18,000
• NASDAQ: Alcista, soporte 18,500

<b>2. Sentimiento</b>
• Riesgo moderado
• Volatilidad contenida

<b>3. Macro</b>
• Sin eventos críticos en apertura europea

<b>4. Escenarios</b>
• SP500: Continuación alcista
• EUR/USD: Rango 1.07–1.08

<b>5. Resumen</b>
Mercado estable, tendencia alcista, riesgo controlado.
"""

# ---------------------------
# Alertas premium
# ---------------------------
def alerta_premium(activo, nivel):
    return f"""
🚨 <b>Alerta Premium</b>
Activo: <b>{activo}</b>
Nivel detectado: <b>{nivel}</b>

<b>Análisis</b>
• Tendencia: Alcista
• Volatilidad: Media
• Probabilidad: Alta
• Riesgo: Controlado

<b>Acción sugerida</b>
Monitorizar estructura y esperar confirmación.
"""

# ---------------------------
# Radar en tiempo real
# ---------------------------
def radar():
    return """
📡 <b>Radar en tiempo real</b>

• SP500: Fuerte impulso
• NASDAQ: Liquidez entrando
• EUR/USD: Rango estrecho
• BTC: Volatilidad creciente
• ORO: Zona de soporte

Actualizado cada minuto.
"""

# ---------------------------
# Comandos premium
# ---------------------------
def comando_premium(activo):
    return f"""
<b>📈 Análisis Premium — {activo}</b>

<b>Estructura</b>
• Tendencia: Alcista
• Soporte: Nivel clave
• Resistencia: Nivel superior

<b>Proyección</b>
• Movimiento esperado: Continuación

<b>Conclusión</b>
Activo en fase técnica favorable.
"""

# ---------------------------
# Webhook
# ---------------------------
@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "").lower()

        # ---------------------------
        # Comandos básicos
        # ---------------------------
        if text == "/start":
            send_message(chat_id, "🤖 Bot premium activo. Usa /resumen, /radar, /alerta, /informe o activos.")
        elif text == "/resumen":
            send_message(chat_id, "📊 Resumen global del mercado:\nSP500 alcista, DAX estable, EUR/USD rango.")
        elif text == "/radar":
            send_message(chat_id, radar())
        elif text == "/informe":
            send_message(chat_id, informe_0600())
        elif text.startswith("/alerta"):
            send_message(chat_id, alerta_premium("SP500", "5200"))
        elif text.startswith("/grafico"):
            send_chart(chat_id, "SP500")

        # ---------------------------
        # Comandos premium por activo
        # ---------------------------
        elif text in ["/sp500", "/nasdaq", "/dax", "/eurusd", "/btc", "/oro"]:
            activo = text.replace("/", "").upper()
            send_message(chat_id, comando_premium(activo))

        else:
            send_message(chat_id, "Comando no reconocido. Usa /resumen, /radar, /informe, /alerta o activos.")

    return {"ok": True}
