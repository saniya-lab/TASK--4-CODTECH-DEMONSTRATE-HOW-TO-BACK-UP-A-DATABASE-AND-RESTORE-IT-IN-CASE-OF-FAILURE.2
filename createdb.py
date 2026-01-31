import sqlite3

# Connect to database (will create if it doesn't exist)
conn = sqlite3.connect("source.db")
cur = conn.cursor()

# Create a table
cur.execute("CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, department TEXT)")

# Insert sample data
cur.execute("INSERT INTO employees (name, department) VALUES ('Alice', 'HR')")
cur.execute("INSERT INTO employees (name, department) VALUES ('Bob', 'Finance')")
cur.execute("INSERT INTO employees (name, department) VALUES ('Charlie', 'IT')")

conn.commit()
conn.close()

print("Source database created successfully!")
