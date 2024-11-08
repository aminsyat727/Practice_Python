def first_last(fl):
    b = []
    b.append(fl[0])
    b.append(fl[-1])

    return b

if __name__ =="__main__":
    a = [5, 10, 15, 20, 25]
    print(first_last(a))
