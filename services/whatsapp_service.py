import requests
import os

CALLMEBOT_API = "https://api.callmebot.com/whatsapp.php"
WHATSAPP_PHONE = os.getenv("WHATSAPP_PHONE")
WHATSAPP_API_KEY = os.getenv("WHATSAPP_API_KEY")

def send_whatsapp_message(message):
    url = f"{CALLMEBOT_API}?phone={WHATSAPP_PHONE}&text={message}&apikey={WHATSAPP_API_KEY}"
    requests.get(url)
