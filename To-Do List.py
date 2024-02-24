def main():
    todo_list = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.append(task)
            print("Task added!")

        elif choice == '2':
            if todo_list:
                print("\nYour To-Do List:")
                for index, task in enumerate(todo_list, 1):
                    print(f"{index}. {task}")
            else:
                print("Your To-Do List is empty!")

        elif choice == '3':
            if todo_list:
                print("\nYour To-Do List:")
                for index, task in enumerate(todo_list, 1):
                    print(f"{index}. {task}")
                task_number = int(input("Enter the task number to mark as done: "))
                if 1 <= task_number <= len(todo_list):
                    del todo_list[task_number - 1]
                    print("Task marked as done!")
                else:
                    print("Invalid task number!")
            else:
                print("Your To-Do List is empty!")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
