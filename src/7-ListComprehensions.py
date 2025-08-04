a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([x for x in a if x%2 == 0])

"""
##Equivalent to the loop below
even =[]
for x in a:
    if x%2 ==0:
        even.append(x)
print(even)
"""