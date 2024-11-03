def get_number(text ="Please give me a number"):
    return (int(input(text)))

##Sieve of Eratosthenes implementation to check for prime numbers. Only works for numbers under 121
def check_small_prime(number):
    #list of integer from 2 to n
    prime = list((range(2, number)))
    #initialize p = 2(smallest prime number)
    p = 2
    #enumarate multiples of p in increment of 2p, 3p to n
    while p <=number:
        for i in range(2*p, number+1, p):
            if i in prime:
                prime.remove(i)

        for j in prime:
            if j > p:
                p = j
                break
        else:
            break
    
    return prime
            

num = get_number("Please select an integer to check for prime number: ")
print(check_small_prime(num))



#prime numbers until 100: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97