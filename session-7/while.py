counter = 0


while (counter < 10):
    if counter == 3:
        counter = counter + 1
        continue
    elif counter == 8:
        counter = counter + 1
        break
    else:
        print(counter)
        counter = counter + 1
