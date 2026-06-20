tasks = []

while True:
    print("\n----- TO DO MANAGER -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        task_name = input("Enter task: ")

        task = {
            "task": task_name,
            "status": "Pending"
        }

        tasks.append(task)

        print("Task added")

    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks")

        else:
            for i, task in enumerate(tasks, start=1):
                print(
                    i,
                    task["task"],
                    "-",
                    task["status"]
                )

    elif choice == "3":

        task_no = int(input("Enter task number: "))

        if 1 <= task_no <= len(tasks):
            tasks[task_no-1]["status"] = "Completed"
            print("Task completed")

        else:
            print("Invalid task number")

    elif choice == "4":

        task_no = int(input("Enter task number: "))

        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no-1)
            print("Task deleted")

        else:
            print("Invalid task number")

    elif choice == "5":
        print("Program closed")
        break

    else:
        print("Invalid choice")