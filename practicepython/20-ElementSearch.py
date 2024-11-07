import random 

def get_number(text ="please select a number between 0-100 : "):
    userinput = int(input(text))
    if userinput < 1 or userinput >= 101:
        userinput = get_number("Wrong input! Please select the number between 0-100 again: ")
    
    return userinput

def search (user,  lst):
    if  user in lst:
        print(True)
    else:
        print(False)

def binary_search(user, lst):
    if len(lst) == 0:
        return False
    
    half  = len(lst)//2
    check = lst[half]
    
    if user == check:
        print("specified element exist in the list")
        return True
    elif user > check:
        lst = lst[half+1:]
        print("Searching in:", lst)
        return binary_search(user, lst)
    else:
        lst = lst[:half]
        print(lst)
        return binary_search(user, lst)



lst = random.sample(range(100), 10)
lst.sort()
user = get_number()
print(binary_search(user, lst))
##search(user, lst)

