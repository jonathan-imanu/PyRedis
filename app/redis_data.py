import sqlite3

class Database():
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE redis_data(
            variable TEXT,
            value BLOB
        )''')
    
    def set(self, variable, value):
        self.c.execute("INSERT INTO redis_data VALUES (:variable, :value)", 
                       {"variable": variable, "value": value})
        self.conn.commit()
    def close(self):
        self.conn.close()





