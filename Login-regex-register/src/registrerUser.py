import os
import json
from user import User

USERS_FILE = "users.json"


def createUser(name, surname, email, password):
    return User(name, surname, email, password)


def validateInputs(name, surname, email, password):
    if not name or not surname or not email or not password:
        return False
    if "@" not in email:
        return False
    if len(password) < 6:
        return False
    return True


def inputUser(nameEntry, surnameEntry, emailEntry, passwordEntry):
    name = input(nameEntry + " : ").strip()
    surname = input(surnameEntry + " : ").strip()
    email = input(emailEntry + " : ").strip()
    password = input(passwordEntry + " : ").strip()

    if validateInputs(name, surname, email, password):
        return createUser(name, surname, email, password)
    return False


def validateUser(user, password):
    return user.password == password


def userExists(email, password):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario.get("email") == email and usuario.get("password") == password:
            return True, usuario
    return False, None


def removeUser(email):
    usuarios = cargar_usuarios()
    nuevos = [u for u in usuarios if u.get("email") != email]
    guardar_usuarios(nuevos)
    return True


def guardar_usuarios(usuarios, ruta=USERS_FILE):
    with open(ruta, "w", encoding="utf-8") as file:
        json.dump(usuarios, file, indent=4, ensure_ascii=False)


def cargar_usuarios(ruta=USERS_FILE):
    if not os.path.exists(ruta):
        with open(ruta, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)
        return []

    with open(ruta, "r", encoding="utf-8") as file:
        return json.load(file)
