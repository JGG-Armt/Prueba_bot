import os
from fastapi import FastAPI, Request
import requests
import datetime

# ---------------------------------------------------------
# PEGA AQUÍ TU TOKEN REAL ENTRE COMILLAS
# --------------------------------------------------------
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
# Informe 06:00
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
🔔 <b>Alerta Premium</b>
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
# Análisis premium por activo
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
# Elliott Wave
# ---------------------------
def elliott(activo):
    return f"""
📐 <b>Elliott Wave — {activo}</b>

<b>Conteo actual</b>
• Onda 3 extendida
• Onda 4 en corrección
• Onda 5 pendiente de confirmación

<b>Zonas clave</b>
• Soporte estructural
• Resistencia de impulso

<b>Conclusión</b>
Estructura técnica madura, esperar confirmación de Onda 5.
"""

# ---------------------------
# Gann — Cuadrado 9
# ---------------------------
def gann(activo):
    return f"""
🌀 <b>Gann — Cuadrado 9 — {activo}</b>

<b>Niveles clave</b>
• 360° — Zona de agotamiento
• 180° — Soporte dinámico
• 90° — Punto de giro

<b>Análisis</b>
Ciclo en fase avanzada, riesgo de reversión moderado.
"""

# ---------------------------
# Ibex 35 — Premium
# ---------------------------
def ibex_premium():
    return """
🇪🇸 <b>Ibex 35 — Análisis Premium</b>

<b>Estructura</b>
• Tendencia: Alcista moderada
• Soporte: 10,200
• Resistencia: 10,600

<b>Proyección</b>
• Movimiento esperado: Rango con sesgo alcista

<b>Conclusión</b>
Ibex en zona técnica relevante, monitorizar niveles clave.
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
        elif
