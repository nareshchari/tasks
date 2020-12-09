import random
startvalue=1
endvalue=10
for genlist_ in range(10):
    randomlist_=[]
    for genval in range(10):
        randomlist_.append(random.randint(startvalue,endvalue))
    startvalue+=10
    endvalue+=10
    print(randomlist_)
