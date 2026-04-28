import sqlite3
conn = sqlite3.connect('training_system.db')
cursor = conn.cursor()
cursor.execute("SELECT employee_no, COUNT(*) as cnt FROM employees GROUP BY employee_no HAVING cnt > 1")
rows = cursor.fetchall()
if rows:
    for row in rows:
        print('Duplicate ACC:', row[0], 'Count:', row[1])
else:
    print('No duplicate ACCs')
conn.close()
