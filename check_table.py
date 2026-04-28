import sqlite3
conn = sqlite3.connect('training_system.db')
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(employees)")
for col in cursor.fetchall():
    print(col)
conn.close()
