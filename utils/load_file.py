import os
import json
import time
from settings.settings import BASE_DIR, BASE_DB


def read_db(username):
    try:
        with open(os.path.join(BASE_DB, '%s_db.json') % username, 'r', encoding='utf-8') as f:
            user_info = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user_info


def write_db(user_info, username):
    try:
        with open(os.path.join(BASE_DB, '%s_db.json') % username, 'w', encoding='utf-8') as f:
            json.dump(user_info, f)
    except Exception:
        return False
