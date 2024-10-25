import itertools
import sqlite3

def generate_combinations(n):
    # Generate all combinations of n letters from the alphabet
    letters = 'abcdefghijklmnopqrstuvwxyz'
    combinations = itertools.product(letters, repeat=n)

    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(f'combinations_with_{n}_letters.db')
    cursor = conn.cursor()

    # Create a table to store combinations
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS combinations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            combination TEXT NOT NULL
        )
    ''')

    # Insert combinations into the database
    for combo in combinations:
        formatted_combo = ''.join(combo).capitalize()
        cursor.execute('INSERT INTO combinations (combination) VALUES (?)', (formatted_combo,))

    # Commit and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    n = int(input("Enter the number of letters (n): "))
    generate_combinations(n)
