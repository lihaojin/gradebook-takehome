from datetime import datetime, timedelta, timezone
import os
from passlib.context import CryptContext
from jose import jwt

JWT_SECRET = os.getenv("JWT_SECRET")
if not JWT_SECRET:
    raise RuntimeError("JWT_SECRET environment variable must be set")

JWT_ALGORITHM = "HS256"
TOKEN_DURATION_MINUTES = 60
REFRESH_TOKEN_DURATION_DAYS = 7

pw_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def verify_password(password_input: str, password_hash: str) -> str:
    return pw_context.verify(password_input, password_hash)

def create_access_token(data: dict, duration_minutes: int = TOKEN_DURATION_MINUTES) -> str:
    data_to_encode = data.copy()
    expiration = datetime.now(timezone.utc) + timedelta(minutes=duration_minutes)

    data_to_encode.update({"exp": expiration})
    return jwt.encode(data_to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)

def create_refresh_token(data: dict) -> str:
    expiration = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_DURATION_DAYS)

    data_to_encode = data.copy()
    data_to_encode.update({"exp": expiration})
    return jwt.encode(data_to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)

# I added this function for future use when we want to decode the 
# token to get the user information
def decode_access_token(token: str) -> dict:
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except Exception as e:
        raise ValueError(f"Invalid token: {e}")
