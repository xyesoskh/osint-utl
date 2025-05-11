import sqlite3

def search_phone(phone):
    conn = sqlite3.connect("db/phones.db")
    c = conn.cursor()
    c.execute("SELECT * FROM phones WHERE phone LIKE ?", (f"%{phone}%",))
    results = c.fetchall()
    conn.close()
    return results

def search_email(email):
    conn = sqlite3.connect("db/leaks.db")
    c = conn.cursor()
    c.execute("SELECT * FROM leaks WHERE email LIKE ?", (f"%{email}%",))
    results = c.fetchall()
    conn.close()
    return results

def search_tg_id(tg_id):
    conn = sqlite3.connect("db/telegram.db")
    c = conn.cursor()
    c.execute("SELECT * FROM telegram WHERE id LIKE ?", (f"%{tg_id}%",))
    results = c.fetchall()
    conn.close()
    return results

def search_tg_username(username):
    conn = sqlite3.connect("db/telegram.db")
    c = conn.cursor()
    c.execute("SELECT * FROM telegram WHERE username LIKE ?", (f"%{username}%",))
    results = c.fetchall()
    conn.close()
    return results
