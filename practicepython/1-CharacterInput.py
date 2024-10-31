from datetime import datetime
name = input("Give me your name?")
print ("your name is " + name)

age = int(input("Give me your age?"))
print ("Your age is " + str(age))

current_year = datetime.now().year
hundred_year = current_year - age + 100
print ("You will be hundred years old by " + str(hundred_year))

