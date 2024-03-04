# Function to add a task to the to-do list
def add_task(todo_list, new_task):
    todo_list.append(new_task)
    print(f"Task '{new_task}' added to the to-do list.")

# Function to remove a task from the to-do list
def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}'removed from the to-do list.")
    else:
        print("Invalid task index. Please choose a valid index.")

def display_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")


# function to Task marked as complete from the to-do list         
def mark_task_complete(todo_list, task_index):
    if task_index >=0 and task_index < len(todo_list):
        todo_list[task_index]["completed"] = True
        print("Task Marked as complete!")

# Main program
todo_list = []

while True:
    print("\n1. Add task")
    print("2. Remove task")
    print("3. Display to-do list")
    print("4. Mark Task As Complete")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        new_task = input("Enter the new task: ")
        add_task(todo_list, new_task)

    elif choice == '2':
        task_index = int(input("Enter the index of the task to remove: "))
        remove_task(todo_list, task_index)

    elif choice == '3':
        display_todo_list(todo_list)

    elif choice == '4':
        task_index = int(input("Enter the index of the task to mark as complete: ")) 
        mark_task_complete(todo_list, task_index)

    elif choice == '5':
        print("Exiting the to-do list program. Goodbye!")

        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")