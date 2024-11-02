##infinite rock paper scissor
import random as rd

rps = ["rock", "paper", "scissor"]
inf = 1

while inf == 1:
    A = input("Player A Rock, Paper, Scissor!!: ").lower()
    while A not in rps:
        print("unidentified input. Please choose again")
        A = input("Player A Rock, Paper, Scissor!!: ").lower()

    B = rd.choice(rps)
    print("Revealing hands:\nA choose: " + A + "\nB choose: " + B)
    while A == "rock":
        if A == B:
            print("Tie")
            break
        elif B == "paper":
            print("B wins")
            break
        else:
            print("A wins")
            break

    while A == "paper":
        if A == B:
            print("Tie")
            break
        elif B == "scissor":
            print("B wins")
            break
        else:
            print("A wins")
            break

    while A == "scissor":
        if A == B:
            print("Tie")
            break
        elif B == "rock":
            print("B wins")
            break
        else:
            print("A wins")
            break
    
    print("\n")