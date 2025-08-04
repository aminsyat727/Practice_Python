num = int(input("please enter a  number: "))

if num % 2 == 0:
    print("The value you specified is an even number")
    if num % 4 == 0:
        print ("The value you specified is also a multiplier of 4")
else:
    print("The value you specified is an odd number")

number = int(input("please enter a number: "))
check = int(input("Please enter the check number: "))

if number % check == 0:
    print("the specified number " + str(number) + " is divisible by " + str(check))
else:
    print ("the specified number " + str(number) + " is not divisible by " + str(check))