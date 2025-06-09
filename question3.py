

todo_list = []

while True:
  
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    

    choice = input("Choose an option : ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append({"task": task, "completed": False})
        print("Task added.")

    elif choice == "2":
        if not todo_list:
            print("No tasks in your to-do list.")
        else:
            
            for i, item in enumerate(todo_list, start=1):
                if item["completed"]:
                    status = "completed"
                else:
                    status = "not completed"
                print(str(i) + ". " + item["task"] + " [" + status + "]")

    elif choice == "3":
        if not todo_list:
            print("No tasks to delete.")
        else:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print("Task '" + removed["task"] + "' deleted.")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if not todo_list:
            print("No tasks to mark.")
        else:
            task_num = int(input("Enter task number to mark completed: "))
            if 1 <= task_num <= len(todo_list):
                todo_list[task_num - 1]["completed"] = True
                print("Task marked as completed.")
            else:
                print("Invalid task number.")

   