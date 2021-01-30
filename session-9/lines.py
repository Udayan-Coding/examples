file = open("book.txt", "r")

text = file.read()

lines = text.split("\n")

print("LIST OF LINES")
print(lines[2])
