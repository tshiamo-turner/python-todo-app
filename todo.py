def show_menu():
  print("\n=== TO-DO LIST MENU ===")
  print("1. View Tasks")
  print("2. Add Task")
  print("3. Remove Task")
  print("4. Exit")
  tasks = []
  while True:
    show_menu()
    choice = input("Enter your choice (1-4):")

if choice =="1":
  if not tasks:
    print("No tasks available")
  else:
    print("\nYour Tasks:")t
    for index, task in enumerate(tasks):
      print(f{index+!}.{task}")

elif choice =="2":
  new_task=input("Enter new tas:")
  tasks.append(new_task)
  print("Task added successfully!")

elif choice=="3":
  if not tasks:
    print("No tasks to remove.")
  else:
    for index, tasks in enumerate(tasks):
      print(f"{index+1}.{task}")
      task_num=int(input("Enter task number to remove:"))
      if 1 <= task_num <= len(tasks):
        removed=tasks.pop(task_num - 1)
        print(f"Removed task:{removed}")
      else:
        print("Invalid task number.")

elif choice == "4":
  print("Goodbye!")
  break

else:
  print("Invalid choice.Please try again.")
