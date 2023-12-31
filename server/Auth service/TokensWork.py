from datetime import datetime, timedelta
from jose import jwt, JWTError
from config import ALGORITHM, TIME_DELTA_FOR_ACCESS, TIME_DELTA_FOR_REFRESH, SECRET_KEY, SYMBOLS_REFRESH_TOKEN
from DatabaseConnect import Database
import random
import string


def create_access_token(user_id: int):
    payload = {"user_id": user_id}

    expire = datetime.utcnow() + timedelta(minutes=TIME_DELTA_FOR_ACCESS)
    payload.update({"exp": expire})
    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def create_refresh_token(user_id: int):
    tokens_data = {}

    token = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(SYMBOLS_REFRESH_TOKEN))
    tokens_data.update({"refresh_token": token})
    tokens_data.update({"created_at": datetime.now()})

    expire = datetime.now() + timedelta(days=TIME_DELTA_FOR_REFRESH)
    tokens_data.update({"exp": expire})
    tokens_data.update({"user_id": user_id})

    return tokens_data


def set_refresh_token(database: Database, user_id):
    tokens_data = create_refresh_token(user_id)
    database.set_token(tokens_data)

    return tokens_data.get("refresh_token")


def update_refresh_token(database: Database, user_id: int):
    tokens_data = create_refresh_token(user_id)
    existing = database.get_info_about_refresh(tokens_data.get("refresh_token"))
    if not existing:
        database.set_token(tokens_data)
    else:
        database.update_token(tokens_data)

    return tokens_data.get("refresh_token")


def validate_access_token(token: str):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return False

    return data.get("exp") >= int(datetime.utcnow().timestamp())


def check_refresh_token(tokens: dict):
    refresh_token = tokens.get("refresh_token")

    database = Database()
    try:
        database.open_connection()

        info_rt = database.get_info_about_refresh(refresh_token)
        print(info_rt)

        if info_rt is not None and int(info_rt[1].timestamp()) >= int(datetime.now().timestamp()):
            database.close_connection()
            return info_rt[0]
    finally:
        database.close_connection()
    return None


def get_user_id(token: str):
    try:
        user_id = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return False

    return user_id.get("user_id")

