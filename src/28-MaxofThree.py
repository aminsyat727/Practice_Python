def largest_of_three(first, second, third):
    list = [first, second, third]
    list.sort()

    return list[-1]

def value(text ="Please specify a numerical value: "):
    value = int(input(text))
    return value

if __name__ =="__main__":
    first = value("First numerical value: ")
    second= value("Second numerical value: ")
    third = value("Third numerical value: ")

    print("The largest value between the three specified value is: " + str(largest_of_three(first, second, third)))