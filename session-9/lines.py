file = open("book.txt", "r")

text = file.read()

lines = text.split("\n")

print("LIST OF LINES")
print(lines)

words = []
for line in lines:
    words += (line.split(" "))

print("LIST OF WORDS")
print(words)
