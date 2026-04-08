import sqlite3
import pandas as pd
from datetime import datetime
import os

DB_PATH = "history.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scan_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            filename TEXT,
            score REAL,
            label TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_scan(filename: str, score: float, label: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO scan_history (timestamp, filename, score, label)
        VALUES (?, ?, ?, ?)
    ''', (timestamp, filename, score, label))
    conn.commit()
    conn.close()

def get_history() -> pd.DataFrame:
    if not os.path.exists(DB_PATH):
        return pd.DataFrame()
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT timestamp, filename, score, label FROM scan_history ORDER BY id DESC", conn)
    conn.close()
    return df
