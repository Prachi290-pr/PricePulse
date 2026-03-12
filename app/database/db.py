import sqlite3
from datetime import datetime

DB_PATH = "data/pricing.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS competitor_prices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        competitor_price REAL,
        source TEXT,
        timestamp TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        predicted_price REAL,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_competitor_price(product_name, price, source):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO competitor_prices (product_name, competitor_price, source, timestamp)
    VALUES (?, ?, ?, ?)
    """, (product_name, price, source, datetime.now()))

    conn.commit()
    conn.close()


def insert_prediction(product_name, predicted_price):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO predictions (product_name, predicted_price, timestamp)
    VALUES (?, ?, ?)
    """, (product_name, predicted_price, datetime.now()))

    conn.commit()
    conn.close()