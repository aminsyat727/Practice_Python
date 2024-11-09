def category_counter(dict, line):
    if len(dict) == 0:
        dict = {line : 1}
    elif line in dict.keys():
        counter  = dict[line]
        counter +=1
        dict[line] = counter
    else:
        dict[line] = 1
    
    return dict


if __name__ == "__main__":
    import re
    counter = {}
    with open('placeholder/nameslist.txt', 'r') as open_file:
        line = open_file.readline()
        while line:
            line = line.replace("\n", "")
            counter = category_counter(counter, line)
            line = open_file.readline()
    print(counter)
    harder_counter = {}
    with open('placeholder/Training_01.txt', 'r') as open_file:
        line = open_file.readline()
        while line:
            line = line.replace("\n", "").split("/", -1)[2]
            harder_counter = category_counter(harder_counter, line)
            line = open_file.readline()
    print(harder_counter)

