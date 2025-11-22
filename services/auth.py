from datetime import datetime, timedelta
import jwt
from decouple import config

JWT_SECRET = config("JWT_SECRET")
JWT_ALG = config("JWT_ALG", default="HS256")

def create_access_token(subject: str, expires_minutes: int = 60):
    exp = datetime.utcnow() + timedelta(minutes=expires_minutes)
    payload = {"sub": subject, "exp": exp}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)
    return token

def decode_token(token: str):
    return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALG])
