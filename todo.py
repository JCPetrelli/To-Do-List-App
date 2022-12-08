import sqlite3

# create a connection to the database
conn = sqlite3.connect("todo.db")

# create a cursor
cursor = conn.cursor()

# create a table for tasks
cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)")

# define a function to add a task to the database
def add_task():
    task=input("Write the task you would like to add...\n")
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    print("Task added successfully")

# define a function to view the list of tasks
def view_tasks():
  cursor.execute("SELECT * FROM tasks")
  rows = cursor.fetchall()
  if len(rows) == 0:
    print("There are no tasks in your to-do list")
  else:
    print("Here is your to-do list:")
    for row in rows:
      print(row[1])

# define a function to remove a task from the database
def remove_task():
    task=input("Write the task you would like to remove...\n")
    cursor.execute("DELETE FROM tasks WHERE task = ?", (task,))
    conn.commit()
    print("Task removed successfully")

# define a function to remove all tasks from the database
def remove_all_tasks():
  cursor.execute("DELETE FROM tasks")
  conn.commit()
  print("All tasks removed successfully")

# define a function to quit the program
def quit_program():
  print("Thank you for using the to-do list program")
  exit()

# create a dictionary of options and their corresponding functions
options = {
  1: add_task,
  2: view_tasks,
  3: remove_task,
  4: remove_all_tasks,
  5: quit_program
}

# run the main program loop
while True:
  print("What would you like to do?")
  print("1. Add a task")
  print("2. View tasks")
  print("3. Remove a task")
  print("4. Remove all tasks")
  print("5. Quit")

  # get the user's choice
  choice = int(input())

  # execute the corresponding function for the chosen option
  options[choice]()

# close the connection to the database
conn.close()