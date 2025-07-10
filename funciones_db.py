import sqlite3
import os

# Crear la carpeta base_datos si no existe
os.makedirs("base_datos", exist_ok=True)

# Ruta de la base de datos
ruta_db = os.path.join("base_datos", "estetica.db")

# Crear tablas si no existen
def crear_tablas():
    with sqlite3.connect(ruta_db) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                whatsapp TEXT,
                email TEXT
            )
        ''')
        conn.commit()

# Registrar un nuevo cliente
def registrar_cliente(nombre, whatsapp, email):
    with sqlite3.connect(ruta_db) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO clientes (nombre, whatsapp, email)
            VALUES (?, ?, ?)
        ''', (nombre, whatsapp, email))
        conn.commit()

# Obtener todos los clientes
def obtener_clientes():
    with sqlite3.connect(ruta_db) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM clientes')
        return cursor.fetchall()

