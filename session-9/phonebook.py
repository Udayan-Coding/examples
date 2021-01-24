# how many numbers do I want to store
number_of_entries = int(input("How many numbers do you want to store?"))

print("Okay, give me name and number respectively for each of them in order")

# create a file to write to
file = open("numbers.txt", "w")

for i in range(0, number_of_entries):
    name = input("Name: ")
    number = input("Number: ")
    entry = f"{name}: {number}\n"
    file.write(entry)
    if i == (number_of_entries - 1):
        print("Done!")
    else:
        print("Okay next one!")

file.close()
