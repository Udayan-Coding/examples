f = open("book.txt", "r+")

text = f.read()

print(text)

f.write("This is a very good book!")

text = f.read()

print(text)

f.close()
