import sqlite3

def create_table():
    con = sqlite3.connect("database/agents.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS agents(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        faction TEXT,
        description TEXT,
        photo_url TEXT
        ) 
    """)
    con.commit()
    con.close()

def add_agent(name,faction,description,photo_url):
    con = sqlite3.connect("database/agents.db")
    cur = con.cursor()
    # Проверяем, есть ли уже такой персонаж с таким name и faction
    cur.execute("""
            SELECT id FROM agents WHERE name = ? AND faction = ?
        """, (name, faction))

    if cur.fetchone():
        print(f"Запись с name='{name}' и faction='{faction}' уже существует. Не вставляем дубли.")
        return

    # Если нет, вставляем новую запись
    cur.execute("""
            INSERT INTO agents (name, faction, description, photo_url) 
            VALUES (?, ?, ?, ?)
        """, (name, faction, description, photo_url))

    con.commit()
    print(f"Добавлена запись: {name} - {faction}")

def find_agent(name):
    con = sqlite3.connect('database/agents.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM agents WHERE name=?', (name, ))
    row = cur.fetchone()
    con.close()
    return row
if __name__ == "__main__":
    create_table()

