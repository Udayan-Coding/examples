file = open("book.txt", "r+")

text = file.read()

print(text)

file.write("This is a very good book!")

file.close()
