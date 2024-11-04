def input_string(text = "Please put some sentences: "):
    return input(text)

def reverse_string(reverse):
    stringlist = reverse.split()
    stringlist.reverse()

    return stringlist

input = input_string()
print(reverse_string(input))