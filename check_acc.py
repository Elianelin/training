import sqlite3
conn = sqlite3.connect('training_system.db')
cursor = conn.cursor()
cursor.execute("SELECT id, employee_no, name, password FROM employees WHERE employee_no LIKE '%linxy28%'")
for row in cursor.fetchall():
    print('ID:', row[0])
    print('ACC repr:', repr(row[1]))
    print('Name:', row[2])
    print('Password repr:', repr(row[3]))
    print('---')
conn.close()
