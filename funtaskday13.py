def mulfun(def_key,def_value,num):
    # empty dictionary
    dictionary={}
    # adding values to dictionary
    dictionary.setdefault(def_key,def_value)
    if len(dictionary)>0:
        # to collect all variable
        svariables = []
        # get values
        for v in dictionary.values():
            # taking each argument
            for i in v:
                # avoiding spaces
                if i != ' ':
                    if i not in svariables:
                        # printing the varibles with repeted times
                        print(f'{i} is repeated {v.count(i)}')
                        # appending variable to list
                        svariables.append(i)
    if num.isnumeric():
        num=int(num)
        if type(num) == int:
            if num >1:
                for i in range(2,num):
                    # if any num is divisible by any number between 2 and n/2 ,it is not prime
                    if (num % i) == 0:
                        print(f"{num} is not a prime number")

                        if num % 3 == 0:
                            print("it is devisible by 3")
                        elif num % 5 == 0:
                            print("it is devisible by 5")

                        break
                    else:
                        print(f"{num} is  a prime number")
                        if (num % 2) == 0:
                            print(f"it is even number")
                        else:
                            print(f"it is odd number")

                        break

        else:
            print("thats not the number")
    else:
        print("please enter the numbers")




def_key="name"
def_value='john james smith'
mulfun(def_key,def_value,num=input("enter number: "))
