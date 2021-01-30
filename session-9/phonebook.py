# how many numbers do I want to store
number_of_entries = int(input("How many numbers do you want to store?"))

print("Okay, give me name and number respectively for each of them in order")

# create a file to write to
file = open("numbers.txt", "w")

"""
    1 2
    0 1
"""
for i in range(0, number_of_entries):
    # asking for a name
    name = input("Name: ")
    # asking the user for a number
    number = input("Number: ")
    # name: number
    entry = f"{name}: {number}\n"  # \n

    file.write(entry)
    if i == (number_of_entries - 1):
        print("Done!")
    else:
        print("Okay next one!")

file.close()
