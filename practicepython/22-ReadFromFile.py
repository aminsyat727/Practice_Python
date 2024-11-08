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
    counter = {}
    with open('nameslist.txt', 'r') as open_file:
        line = open_file.readline()
        while line:
            line = line.replace("\n", "")
            counter = category_counter(counter, line)
            line = open_file.readline()
    print(counter)

