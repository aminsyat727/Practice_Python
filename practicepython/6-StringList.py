a = str(input("Please insert a string: ").lower())

print(a)
print(a[::-1])

if a == a[::-1]:
    print("Palindrome")
else:
    print("not palindrome")

