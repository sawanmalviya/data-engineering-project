import sqlite3

DB_PATH = "db/data.db"

def create_table():
    """Creates a table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            amount REAL
        )
    """)
    conn.commit()
    conn.close()

def insert_transaction(name, amount):
    """Inserts a transaction record."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (name, amount) VALUES (?, ?)", (name, amount))
    conn.commit()
    conn.close()

def fetch_transactions():
    """Fetches all transactions."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    create_table()
    insert_transaction("Alice", 100.50)
    print(fetch_transactions())
