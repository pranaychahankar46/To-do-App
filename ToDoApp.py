def task():
    tasks = []  # Empty list to store tasks
    print("---- WELCOME TO TASK MANAGEMENT APP ----")

    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are:\n{tasks}")

    while True:
        print("MENU:")
        print("1 - Add Task")
        print("2 - Update Task")
        print("3 - Delete Task")
        print("4 - View Tasks")
        print("5 - Exit/Stop")
        
        operation = int(input("Enter your choice : "))
        
        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                new_task = input("Enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = new_task
                print(f"Task '{updated_val}' has been updated to '{new_task}'.")
            else:
                print(f"Task '{updated_val}' not found.")

        elif operation == 3:
            delete_val = input("Enter the task name you want to delete = ")
            if delete_val in tasks:
                tasks.remove(delete_val)
                print(f"Task '{delete_val}' has been deleted.")
            else:
                print(f"Task '{delete_val}' not found.")

        elif operation == 4:
            print("Today's tasks are :")
            for task in tasks:
                print(task)

        elif operation == 5:
            print("Exiting Task Management App. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    task()