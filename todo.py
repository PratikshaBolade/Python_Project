import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Pbolade@20',
    database='mydatabase'
)


def add_task(tasks, task_name, priority, due_date):
    cursor = db.cursor()
    sql = 'INSERT INTO tasks (task_name,priority,due_date) VALUES (%s,%s,%s)'
    val = (task_name, priority, due_date)
    cursor.execute(sql, val)
    db.commit()
    print(f"Task '{task_name}' added.")


def remove_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        cursor = db.cursor()
        sql = 'DELETE FROM tasks WHERE id = %s'
        val = (task_index,)
        cursor.execute(sql, val)
        db.commit()
        print(f"Task removed.")
    else:
        print("Invalid task index.")


def complete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        cursor = db.cursor()
        sql = 'UPDATE tasks SET status = 1 WHERE id = %s'
        val = (task_index,)
        cursor.execute(sql, val)
        db.commit()
        print(f"Task marked as completed.")
    else:
        print("Invalid task index.")


def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        cursor = db.cursor()
        sql = 'SELECT * FROM tasks'
        cursor.execute(sql)
        tasks = cursor.fetchall()
        db.commit()
        if tasks:
            for task in tasks:
                print(f"{task[0]}. {task[1]} (Priority: {task[2]}, Due Date: {task[3]},"
                      f" Status: {'completed' if task[4] else 'Pending'})")


# Main function
def main():
    def load_tasks():
        cursor = db.cursor()
        sql = 'SELECT * FROM tasks'
        cursor.execute(sql)
        records = cursor.fetchall()
        db.commit()
        for record in records:
            return record
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. View Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            priority = input("Enter task priority (high, medium, low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, task_name, priority, due_date)
        elif choice == "2":
            display_tasks(tasks)
            task_index = int(input("Enter the index of the task to remove: "))
            remove_task(tasks, task_index)
        elif choice == "3":
            display_tasks(tasks)
            task_index = int(input("Enter the index of the task to mark as completed: "))
            complete_task(tasks, task_index)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
