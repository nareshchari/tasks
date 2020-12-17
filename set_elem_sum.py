def add_set_ele(*any):
    total = 0
    for elem in any:
        vals = set(tuple(elem))
        for i in vals:
            total += int(i)
    print(total)




if __name__ == "__main__" :
    uinput = input("enter values: ").split(' ')
    add_set_ele(uinput)


