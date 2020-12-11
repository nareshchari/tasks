# exercise 1:copy method
list_ = [1,1.5,'python',0b101,True,[20+10j,"india",range(10)]]
newlist_ = list_.copy()
print(list_)
print(newlist_)
# if we make any changes the parent copy it also changing in child copy why?
# what is deep copy and shallow copy?
list_[5].append("john")
print(list_)
print(newlist_)

#exercise 2:using extend
# case 1:the list only contins sub lists no values
list_=[[1,23,3],[5,4,4,5],[78,54,54,69]]
newlist_ = []
for lelements in list_:
    # extending inner list with empty new list
    newlist_.extend(lelements)
print(f'\ncase 1:the list only contins sub lists no values\n{newlist_}')
# list comprehension
print(f'\nlist comprehension\n{[k for lele in list_ for k in lele]}')

# case 2:the list contins sub lists and values
list_=[[1,23,3],[5,4,4,5],[78,54,54,69],58,96,6,"hello",6,56,4,]
newlist_ = []
for lelements in list_:
    # checking inner list type is list or not
    if type(lelements) is list:
        newlist_.extend(lelements)
    else:
        newlist_.append(lelements)
print(f'\ncase2: the list contins sub lists and values \n{newlist_}')

# exercise 3:shop
tshirts_colour = ['white','black']
tshirts_sizes = ['Small','Medium','Large',"XtraLarge"]
diff_size_tshirts = []
for color in tshirts_colour:
    for size in tshirts_sizes:
        # printing all available tshirst colors and its sizes
        print(f'\n "{color}" color "{size}" size tshirt')




#exercise 4:find duplicate value of index
l = [1,2,2,2,2,3,4,5,6,7,8,9,1,45,54,54,46,58,4,5]
# empty list to collect duplicate values
duplicate = []
for i in range(len(l)):
    # taking next value of previous loop starting value
    k=i+1
    for j in range(k,len(l)):
        # checking 1st value with next values and the value present in duplicate or not
        if l[i] == l[j] and l[i] not in duplicate:
            # appending the duplicate values
            duplicate.append(l[i])
            # printing the duplicate values index values
            print(f'\nthe duplicate element is {l[i]} and its index is {l.index(l[i],l.index(l[i])+1)}')





# exercise 5:
list_1 = [[1,2,3,4],[2,3,4],[1,3,4,5,6],[1,2],[1],2]
for inerl in list_1:
    # to avoid integers
    if type(inerl) != int:
        # if list contains more than two values
        if len(inerl) > 2:
            # to keep only two values in nested list
            while len(inerl) > 2:
                    inerl.pop()
        # To avoid if list has only 2 values
        elif len(inerl) == 2:
            pass


print(f'\n{list_1}')

# exercise 6:list comprehension

tshirts_colour = ['white','black']
tshirts_sizes = ['Small','Medium','Large',"XtraLarge"]
# list comprehnsion
data=[f'"{size}" size "{color}" color tshirt' for size in tshirts_sizes for color in tshirts_colour]
# printing each statement in data
for i in data:
    print(f'\n{i}')


