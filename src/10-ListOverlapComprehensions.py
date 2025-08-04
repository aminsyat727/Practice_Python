import random

a = random.sample(range(20), 10)
b = random.sample(range(20), 15)

print(a)
print(b)

new_list = [x for x in a if x in b]
print(new_list)

