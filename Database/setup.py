import sqlite3

def create_db():
    conn = sqlite3.connect('TODO_TABLE.db')
    conn.execute('PRAGMA foreign_keys = ON')

    conn.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id_user INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    );
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS userDetails (
        id_user_details INTEGER PRIMARY KEY,
        id_user INTEGER,
        phone_number TEXT,
        address TEXT,
        preference TEXT,
        FOREIGN KEY (id_user) REFERENCES Users(id_user)
    );
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS Tasks (
        id_task INTEGER PRIMARY KEY,
        id_user INTEGER,
        description TEXT,
        status TEXT,
        due_date TEXT,
        FOREIGN KEY (id_user) REFERENCES Users(id_user)
    );
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS Tags (
        id_tag INTEGER PRIMARY KEY,
        name TEXT
    );
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS task_tag (
        id_task INTEGER,
        id_tag INTEGER,
        FOREIGN KEY (id_task) REFERENCES Tasks(id_task),
        FOREIGN KEY (id_tag) REFERENCES Tags(id_tag),
        PRIMARY KEY (id_task, id_tag)
    );
    """)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()