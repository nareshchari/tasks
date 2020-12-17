import random

def tuple_to_dict(t):
    # checking tuple type
    if type(t) == tuple:
        # generating random values and adding to the tuple
        t = t+tuple(random.randint(1,1000) for i in range(1,5))
        # empty dictionary
        ditems = {}
        # adding tuple items as keys to dictionary and generating random value makin value to dictionary
        for i in t:
            ditems[i]=random.randint(1,10000)
        print(ditems)
    # if it is a not tuple it exicutes
    else:
        print("please enter tuple")


if __name__ == "__main__":
    for i in range(1,21):
        t=tuple()
        tuple_to_dict(t)
