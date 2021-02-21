# fn(arg) -> num

def addNum(number):
    addition = 0
    for i in range(1, number + 1):
        addition += i
    return addition


result = addNum(4)

print(result)
