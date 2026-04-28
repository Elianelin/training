import sqlite3
conn = sqlite3.connect('training_system.db')
cursor = conn.cursor()
cursor.execute("SELECT id, employee_no, name, password FROM employees WHERE employee_no = 'linxy28'")
row = cursor.fetchone()
if row:
    print('ID:', row[0])
    print('ACC:', row[1])
    print('Name:', row[2])
    print('Password:', repr(row[3]))
else:
    print('Employee not found')
conn.close()
