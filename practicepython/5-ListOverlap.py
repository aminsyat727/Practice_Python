import random as rd

a = rd.sample(range(20), 10)
b = rd.sample(range(20), 15)
c = []

print(a)
print(b)

for elem in a:
    if elem in b:
        c.append(elem)

print("These are the numbers that are overlapping between the two list " + str(c))