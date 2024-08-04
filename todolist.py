import sqlite3

conn = sqlite3.connect(r'todolist\todo.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')
conn.commit()

def display_menu():
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task():
    while True:
        task = input("Enter the task description: ")
        if task.strip() == "":
            print("Please enter a valid task.")
        else:
            cursor.execute('''
            INSERT INTO users (name)
            VALUES (?)
            ''', (task,))
            conn.commit()
            print(f'Task "{task}" added.')
            break

def view_tasks():
    cursor.execute('SELECT id, name FROM users')
    rows = cursor.fetchall()
    if not rows:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for row in rows:
            print(f"{row[0]}. {row[1]}")

def remove_task():
    view_tasks()
    try:
        task_id = int(input("Enter the task ID to remove: "))
        cursor.execute('DELETE FROM users WHERE id = ?', (task_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f'Task ID "{task_id}" removed.')
        else:
            print("Invalid task ID.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
    conn.close()
