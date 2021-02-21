# bubble sort

ls = [3, 14, 8, 2, 20]  # n
n = len(ls)

for i in range(n):
    for j in range(n - i - 1):
        if ls[j] > ls[j + 1]:
            temp = ls[j]
            ls[j] = ls[j + 1]
            ls[j + 1] = temp

print(ls)
