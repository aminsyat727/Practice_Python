##infinite guessing game
import random as rd
inf = 1
while inf == 1:
    a = rd.randint(0, 9)   
    guess = 1000

    while guess != a:
        guess = int(input("Please select a number between 0 to 9: "))
        if guess == a:
            print("Congrats! you guess the correct value")
            break
        elif guess >= a:
            (print("lower"))
        elif guess <= a:
            print("higher")
        else:
            pass

    print("\nstarting new guessing game")
