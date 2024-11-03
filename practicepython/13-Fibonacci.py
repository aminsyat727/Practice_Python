#fibonacci sequence. For this case we consider the fibonacci sequence start from 1

def user_input(text ="How many fibonacci sequence you want to be generated: "):
    return int(input(text))
    
def fibonacci_sequence(n):
    for i in range(n):
        if i  == 0:
            F =[0]
        elif i <= 1:
            F.append(1)
        else:
            Fibo = F[i-1] + F[i-2]
            F.append(Fibo)
    return F

fibo = user_input()
print(fibonacci_sequence(fibo))









