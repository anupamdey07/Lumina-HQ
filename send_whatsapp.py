# logic to send news via WhatsApp Business API

# news_pulse/send_whatsapp.py
import os
import requests

TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_ID = os.getenv("PHONE_ID")
TO_PHONE = os.getenv("TO_PHONE_NUMBER")

URL = f"https://graph.facebook.com/v19.0/{PHONE_ID}/messages"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "messaging_product": "whatsapp",
    "to": TO_PHONE,
    "type": "text",
    "text": {
        "body": "📰 Daily News Pulse Test — If you got this, we're live!"
    }
}

res = requests.post(URL, json=payload, headers=headers)
print(res.status_code)
print(res.text)
