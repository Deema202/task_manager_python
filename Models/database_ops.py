import sqlite3

def get_connection():
    conn = sqlite3.connect('TODO_TABLE.db')
    conn.execute('PRAGMA foreign_keys = ON;')
    return conn

# Users
def read_users():
    conn = get_connection()
    crsor = conn.execute("SELECT * FROM Users;")
    users = crsor.fetchall()
    conn.close()
    return users

def read_user(id_user):
    conn = get_connection()
    crsor = conn.execute('SELECT * FROM Users WHERE id_user=?;', (id_user,))
    user = crsor.fetchone()
    conn.close()
    return user

def create_user(name, email):
    conn = get_connection()
    conn.execute('INSERT INTO Users (name, email) VALUES (?,?);', (name, email))
    conn.commit()
    conn.close()

def update_user(id_user, name, email):
    conn = get_connection()
    conn.execute('UPDATE Users SET name=?, email=? WHERE id_user=?;', (name, email, id_user))
    conn.commit()
    conn.close()

def delete_user(id_user):
    conn = get_connection()
    conn.execute('DELETE FROM Users WHERE id_user=?;', (id_user,))
    conn.commit()
    conn.close()

# userDetails
def read_user_details():
    conn = get_connection()
    crsor = conn.execute("SELECT * FROM userDetails;")
    users = crsor.fetchall()
    conn.close()
    return users

def read_user_detail(id_user_details):
    conn = get_connection()
    crsor = conn.execute('SELECT * FROM userDetails WHERE id_user_details=?;', (id_user_details,))
    user = crsor.fetchone()
    conn.close()
    return user

def view_user_details(id_user):
    conn = get_connection()
    crsor = conn.execute("""
        SELECT U.id_user, U.name, U.email,
               D.phone_number, D.address, D.preference
        FROM Users U
        LEFT JOIN userDetails D ON U.id_user = D.id_user
        WHERE U.id_user = ?;
    """, (id_user,))
    user_details = crsor.fetchone()
    conn.close()
    return user_details

def create_user_details(id_user, phone_number, address, preference):
    conn = get_connection()
    conn.execute('INSERT INTO userDetails (id_user, phone_number, address, preference) VALUES (?,?,?,?);',
                 (id_user, phone_number, address, preference))
    conn.commit()
    conn.close()

def update_user_details(id_user_details, phone_number, address, preference):
    conn = get_connection()
    conn.execute('UPDATE userDetails SET phone_number=?, address=?, preference=? WHERE id_user_details=?;',
                 (phone_number, address, preference, id_user_details))
    conn.commit()
    conn.close()

def delete_user_details(id_user_details):
    conn = get_connection()
    conn.execute('DELETE FROM userDetails WHERE id_user_details=?;', (id_user_details,))
    conn.commit()
    conn.close()

# Tasks
def read_tasks():
    conn = get_connection()
    crsor = conn.execute("SELECT * FROM Tasks;")
    tasks = crsor.fetchall()
    conn.close()
    return tasks

def read_task(id_task):
    conn = get_connection()
    crsor = conn.execute('SELECT * FROM Tasks WHERE id_task=?;', (id_task,))
    task = crsor.fetchone()
    conn.close()
    return task

def create_task(id_user, description, status, due_date):
    conn = get_connection()
    conn.execute('INSERT INTO Tasks (id_user, description, status, due_date) VALUES (?,?,?,?);',
                 (id_user, description, status, due_date))
    conn.commit()
    conn.close()

def update_task(id_task, description, status, due_date):
    conn = get_connection()
    conn.execute('UPDATE Tasks SET description=?, status=?, due_date=? WHERE id_task=?;',
                 (description, status, due_date, id_task))
    conn.commit()
    conn.close()

def delete_task(id_task):
    conn = get_connection()
    conn.execute('DELETE FROM Tasks WHERE id_task=?;', (id_task,))
    conn.commit()
    conn.close()

def mark_task_complete(id_task):
    conn = get_connection()
    conn.execute("UPDATE Tasks SET status=? WHERE id_task=?;", ("Completed", id_task))
    conn.commit()
    conn.close()

# Tags
def read_tags():
    conn = get_connection()
    crsor = conn.execute("SELECT * FROM Tags;")
    tags = crsor.fetchall()
    conn.close()
    return tags

def read_tag(id_tag):
    conn = get_connection()
    crsor = conn.execute("SELECT * FROM Tags WHERE id_tag = ?;", (id_tag,))
    tag = crsor.fetchone()
    conn.close()
    return tag

def create_tag(name):
    conn = get_connection()
    conn.execute('INSERT INTO Tags (name) VALUES (?);', (name,))
    conn.commit()
    conn.close()

def update_tag(id_tag, name):
    conn = get_connection()
    conn.execute('UPDATE Tags SET name=? WHERE id_tag=?;', (name, id_tag))
    conn.commit()
    conn.close()

def delete_tag(id_tag):
    conn = get_connection()
    conn.execute('DELETE FROM Tags WHERE id_tag=?;', (id_tag,))
    conn.commit()
    conn.close()

# task_tag
def read_task_tags():
    conn = get_connection()
    crsor = conn.execute("SELECT * FROM task_tag;")
    task_tags = crsor.fetchall()
    conn.close()
    return task_tags

def read_task_tag(id_task, id_tag):
    conn = get_connection()
    crsor = conn.execute("SELECT * FROM task_tag WHERE id_task=? AND id_tag=?;", (id_task, id_tag))
    task_tag = crsor.fetchone()
    conn.close()
    return task_tag

def create_task_tag(id_task, id_tag):
    conn = get_connection()
    conn.execute('INSERT INTO task_tag (id_task, id_tag) VALUES (?,?);', (id_task, id_tag))
    conn.commit()
    conn.close()

def update_task_tag(id_task, old_id_tag, new_id_tag):
    conn = get_connection()
    conn.execute('UPDATE task_tag SET id_tag=? WHERE id_task=? AND id_tag=?;', (new_id_tag, id_task, old_id_tag))
    conn.commit()
    conn.close()

def delete_task_tag(id_task, id_tag):
    conn = get_connection()
    conn.execute('DELETE FROM task_tag WHERE id_task=? AND id_tag=?;', (id_task, id_tag))
    conn.commit()
    conn.close()

# Extra Reads
def list_tags_for_task(id_task):
    conn = get_connection()
    crsor = conn.execute("""
        SELECT T.name
        FROM Tags T
        JOIN task_tag TT ON T.id_tag = TT.id_tag
        WHERE TT.id_task = ?;
    """, (id_task,))
    tags = crsor.fetchall()
    conn.close()
    return tags

def list_tasks_for_tag(id_tag):
    conn = get_connection()
    crsor = conn.execute("""
        SELECT T.description
        FROM Tasks T
        JOIN task_tag TT ON T.id_tag = TT.id_tag
        WHERE TT.id_tag = ?;
    """, (id_tag,))
    tasks = crsor.fetchall()
    conn.close()
    return tasks