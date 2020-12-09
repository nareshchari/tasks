vowels = "aeiou"
# no need for cpital alpha because we are making user input into lower case
alnum_ = "abcdefghijklmnopqrstuvwxyz0123456789"
temp = 0
while True:
    # taking input from user and modifying into lowercase to avoid case sensitive and removing spaces before and after
    statement = input("\nEnter your input: ").lower().strip()
    # to avoid single spce
    statement = statement.replace(' ','')
    if statement != "":
        for each_char in statement:
            k = statement.find(each_char,statement.index(each_char)+1,len(statement))
            if k == -1:
                temp += 1
                if each_char in vowels:
                    print(f"\nunique character is {each_char} and is vowel\n")
                elif each_char in "0123456789":
                    # not considering numbers
                    pass
                # checking symbol or not
                elif each_char not in alnum_:
                    print(f"\n{each_char}  is symbol and  {each_char.encode()} encoded value  of symbols\n")
                else:
                    print(f"\nunique character is {each_char} and is consonent\n")
        if temp == 0:
            print("\nThere is no unique letter\n")
        # taking user decission
        user_input = input("\nwould you like to continue y/n..? :").lower()
        if user_input != 'y':
            break
        else:
            pass
    else:
        print("\nplease enter valid input\n")

