from colored import fg, bg, attr


# Let the user know about options
help_text = "Welcome to todo-management\nPress 1 for seeing all the todo.\nPress 2 for adding a todo.\nPress 3 for deleting a todo."


choice = input(help_text + "\n> ")

if choice == "1":
    # open the file
    try:
        # check if the file exists
        file = open("todo.txt", "r+")
    except:
        # if the file does not exist
        print("No todos exists at the moment.")
        exit()

    # get the todos as an array
    todos = file.read().split("\n")
    # remove empty strings from the array
    todos.remove('')

    # if there are no todos
    if len(todos) == 0:
        color = fg("red")
        reset = attr("reset")
        print(color + "No todos exists at the moment." + reset)
        exit()

    color = fg("yellow")
    reset = attr("reset")
    # prints the todos
    for i in range(0, len(todos)):
        print(f"{color} [{i + 1}] {todos[i]} {reset}")

    # close the file
    file.close()

elif choice == "2":
    # get the todo to add
    todo = input("Enter the todo to add: ")
    # open the file in append mode
    file = open("todo.txt", "a")
    # write the todo to the file
    file.write(todo + "\n")
    # close the file
    file.close()

elif choice == "3":
    # get the todos
    file = open("todo.txt", "r+")
    todos = file.read().split("\n")
    todos.remove('')

    # print the todos  once again
    for i in range(0, len(todos)):
        print(f"[{i + 1}] {todos[i]}")
    # close file
    file.close()
    # open the file
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
