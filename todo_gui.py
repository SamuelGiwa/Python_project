import sqlite3
import tkinter as tk
from tkinter import messagebox

# Set up the database
conn = sqlite3.connect(r'todolist\todo.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')
conn.commit()

def add_task_to_db(task):
    cursor.execute('''
    INSERT INTO users (name)
    VALUES (?)
    ''', (task,))
    conn.commit()

def get_all_tasks():
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

def add_task():
    task = task_entry.get()
    if task.strip() == "":
        messagebox.showwarning("Input Error", "Please enter a valid task.")
    else:
        add_task_to_db(task)
        task_entry.delete(0, tk.END)
        update_task_list()

def remove_task():
    task = task_entry.get()
    try:
        task_id = int(task)
        cursor.execute('DELETE FROM users WHERE id = ?', (task_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f'Task ID "{task_id}" removed.')
        else:
            print("Invalid task ID.")
        update_task_list()
        task_entry.delete(0, tk.END)
    except ValueError:
        print("Please enter a valid number.")

def update_task_list():
    task_list.delete(0, tk.END)
    for row in get_all_tasks():
        task_list.insert(tk.END, f"{row[0]}. {row[1]}")

def on_closing():
    conn.close()
    root.destroy()

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=20)

task_entry = tk.Entry(frame, width=40)
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

add_button = tk.Button(frame, text="Remove Task", command=remove_task)
add_button.pack(side=tk.LEFT)

task_list = tk.Listbox(root, width=50, height=15)
task_list.pack(pady=20)

update_task_list()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()