
my_list = [4, 7, 2, 8, 3, 4, 7, 1, 9, 2, 5, 3, 6, 8, 5, 10]
print("this is the original list\n" +str(my_list))


def remove_duplicate_loop(a):
    loop_list = []
    for x in a:
        if len(loop_list) == 0:
            loop_list.append(x)
        elif len(loop_list) <= len(a)+1:
            if x in loop_list:
                pass
            else:
                loop_list.append(x)
        else:
            break
    
    return loop_list
            
def remove_duplicate_sets(b):
    set_list = set(b)
    return set_list

print("removing duplicate from list using loop\n" + str(remove_duplicate_loop(my_list)))
print("removing duplicate from list using set\n" + str(remove_duplicate_sets(my_list)))

