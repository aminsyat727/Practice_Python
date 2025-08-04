def input_string(text = "Please put some sentences: "):
    return input(text)

def reverse_string(reverse):
    stringlist = reverse.split()
    stringlist.reverse()

    return stringlist

if __name__=="__main__":
    input = input_string()
    print(reverse_string(input))