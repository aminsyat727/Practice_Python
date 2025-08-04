import random as rd

a = rd.sample(range(20), 10)
b = rd.sample(range(20), 15)

print("a: " + str(a))
print("b: " + str(b))

def overlap_loop(a, b):
    c = []
    for elem in a:
        if elem in b:
            c.append(elem)
    return c

def overlap_set(a, b):
    A = set(a) 
    B = set(b)
    c = list(A&B)
    return c
    

print("overlapping list filtered using loop\n" + str(overlap_loop(a, b)))
print("overlapping list filtered using set\n" + str(overlap_set(a, b)))