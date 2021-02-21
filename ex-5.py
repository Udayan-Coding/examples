ls = [3, 14, 8, 2, 2, 6, 14, 3, 9, 14]

maximum = max(ls)

frequency = ls.count(maximum)

indexes = list()

for i in range(len(ls)):
    if ls[i] == maximum:
        indexes.append(i)


print("Maximum Number:", maximum)
print("Frequency of Number:", frequency)
print("Indexes of Maximum:", indexes)
