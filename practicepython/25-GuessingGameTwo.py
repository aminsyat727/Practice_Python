complist = list (range(100))
print(complist)
count = 0
while True:
    half = len(complist)//2
    ask = input ("Is the number " + str(complist[half]) + " (correct/higher/lower)? " )

    if ask == "higher" and half != 1:
        complist = complist[half:]
        count +=1
    elif ask == "lower" and half !=1:
        complist = complist[:half+1]
        count +=1
    elif ask == "correct":
        print("you guess the correct number")
        count +=1
        break
    elif half ==1:
        print("not possible, restarting the guess")
        complist = list(range(100))
        count = 0
    else:
        print("wrong input, please specify the again")
    
print("you took " + str(count) +" guess")