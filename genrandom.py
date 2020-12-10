import random
# to get different lists  doesnt contain same values in between lists
startvalue=1
endvalue=10
for genlist_ in range(10):
    # getting each time fresh list
    randomlist_=[]
    for genval in range(10):
        # generating random values and appending in list
        randomlist_.append(random.randint(startvalue,endvalue))
    startvalue+=10
    endvalue+=10
    print(randomlist_)
