# Let the user know about options
help_text = "Welcome to todo-management\nPress 1 for seeing all the todo.\nPress 2 for adding a todo.\nPress 3 for deleting a todo."


choice = input(help_text + "\n> ")

if choice == "1":
    # open the file
    file = open("todo.txt", "r+")
    todos = file.read().split("\n")
    print(todos)
    file.close()
elif choice == "2":
    todo = input("Enter the todo to add: ")
    file = open("todo.txt", "a")
    file.write(todo + "\n")
    file.close()
elif choice == "3":
    # get the todos
    file = open("todo.txt", "r+")
    todos = file.read().split("\n")
    for i in range(0, len(todos)):
        print(f"[{i + 1}] {todos[i]}")
    file.close()
    file = open("todo.txt", "w")
    # get the todo number to be deleted
    todo_number = int(input("Enter the todo number to be deleted: "))
    todos.pop(todo_number - 1)
    for i in range(0, len(todos)):
        file.write(todos[i] + "\n")
    file.close()
else:
    print("That is not a valid option.")
    print(help_text)
print(choice)
