# user_auth.py
import streamlit as st
import json
import os
import bcrypt

USER_DATA_FILE = "./notebook_app/auth/users.json"

class UserAuth:
    def __init__(self):
        if not os.path.exists(USER_DATA_FILE):
            with open(USER_DATA_FILE, "w") as f:
                json.dump({}, f)

    def _load_users(self):
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)

    def _save_users(self, users):
        with open(USER_DATA_FILE, "w") as f:
            json.dump(users, f)

    def register_user(self, username, password):
        users = self._load_users()
        if username in users:
            raise ValueError("Usuário já existe!")
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        users[username] = {"password": hashed}
        self._save_users(users)

    def authenticate(self, username, password):
        users = self._load_users()
        user = users.get(username)
        if user and bcrypt.checkpw(password.encode(), user["password"].encode()):
            return True
        return False