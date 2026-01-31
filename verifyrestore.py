import sqlite3

conn = sqlite3.connect("source.db")
cur = conn.cursor()

# Fetch all data from employees table
cur.execute("SELECT * FROM employees")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
