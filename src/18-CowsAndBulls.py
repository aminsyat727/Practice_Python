def user_input (text = "Enter 4 digit numbers: "):
    userinput = (input(text))
    userinput = [int(i) for i in str(userinput)]
    if len(userinput) <= 3:
        userinput = (input("Not enough digit, please enter 4 digit numbers again: "))

    return userinput

def randomgenerator():
    y = []
    for i in range(0, 4):
        x = random.randrange(9)
        y.append(int(x))

    return y 

def cows (userinput, random):
    cow = 0
    x = 0
    for i in userinput:
        if i == random[int(x)]:
            cow +=1
        else:
            pass
        x += 1

    return cow

def bulls (userinput, random):
    bull = 0
    x = 0
    for i in userinput:
        if i != random[int(x)]:
            bull +=1
        else:
            pass
        x += 1
    
    return bull


if __name__=="__main__":
    import random 
    print("Welcome to the Cows and Bulls Game!")
    cowbull = randomgenerator()

    cow = 0
    while cow != 4:
        user = user_input()
        cow = cows(user, cowbull)
        bull = bulls(user, cowbull)
        print(str(cow) + " cows, " + str(bull) + " bulls")
    
    print("Congrats! You guess the right numbers!")