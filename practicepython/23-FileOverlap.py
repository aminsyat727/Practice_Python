overlap_list = []
with open('placeholder/primenumbers.txt', 'r') as prime_file:
    main_text = prime_file.read().replace("\n", "")
with open('placeholder/happynumbers.txt', 'r') as happy_file:
    line = happy_file.readline().replace("\n", "")
    while line:
        if line in main_text:
            overlap_list.append(int(line))
        line = happy_file.readline().replace("\n", "") 

print(overlap_list)