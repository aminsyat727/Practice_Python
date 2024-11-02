num = int(input("Please select a number: "))
a = range(1, num)
b = []
for i in range(len(a)):
    if num % a[i] == 0:
        b.append(a[i])
    else:
        continue

if len(b) != 0:
    print("The number specified are divisible by " + str(b)) 
else:
    print ("The number specified has no divisible number")
          