import random
a = random.sample(range(20), 10)
print ("The variable a is a " + str(type(a)))
print("It can fill in up to " + str(len(a)) +" values")
print(a)
b = []
for i in range(len(a)):

    if a[i] <= 10:
        b.append(a[i])
    else:
        continue

print("Here's a new list with number less than ten " + str(b))