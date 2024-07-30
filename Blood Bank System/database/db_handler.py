import sqlite3

def create_tables():
    conn = sqlite3.connect('blood_bank.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS donors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    blood_type TEXT NOT NULL,
                    contact TEXT NOT NULL)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS blood_units (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    donor_id INTEGER,
                    blood_type TEXT NOT NULL,
                    donation_date TEXT NOT NULL,
                    expiration_date TEXT NOT NULL,
                    FOREIGN KEY(donor_id) REFERENCES donors(id))''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS recipients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    blood_type TEXT NOT NULL,
                    contact TEXT NOT NULL,
                    request_date TEXT NOT NULL)''')
    
    conn.commit()
    conn.close()

def insert_donor(donor):
    conn = sqlite3.connect('blood_bank.db')
    c = conn.cursor()
    c.execute('INSERT INTO donors (name, blood_type, contact) VALUES (?, ?, ?)', 
              (donor.name, donor.blood_type, donor.contact))
    conn.commit()
    conn.close()

def get_all_donors():
    conn = sqlite3.connect('blood_bank.db')
    c = conn.cursor()
    c.execute('SELECT * FROM donors')
    donors = c.fetchall()
    conn.close()
    return donors

if __name__ == "__main__":
    create_tables()
