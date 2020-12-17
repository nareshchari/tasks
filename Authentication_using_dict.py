
def authenticate():
    user_data = {"David":"David@121",
                    "john":"stepsy@$",
                    "nova":"nancy"}
    # if loggin success it will True else by default it's false
    success = False
    # to count the login atempts taken temp variable
    lcount = 0
    while True:
        # asking user to enter credentials
        uname = input("\nEnter your username: ")
        password = input("\nEnter your password: ")

        # checking the credentials
        for uname_,password_ in user_data.items():
            if uname_ == uname and password_ == password:
                print("successfully loged in ")
                success = True
        # checking the login success
        if not success:
            # counting the login atempts
            lcount += 1
            # if attempts reach maximum
            if lcount == 3:
                print("\nExceeded maximum limit")
                break
            print("\none of your username or password not matched please try again")
        else:
            break
authenticate()



# i = 1
# while i<4:
#     username_password = {"siri":"0000"}
#     name = input("enter username:\n")
#     passcode = input("enter password:\n")


#     i+=1
#     if username_password.get(name) == passcode:
#         print("successfully logged in")
#         break
#     else:
#         print("username and passcode not matched")
# else:
#     print("attempted maximum")






def id_password():
    dict_ = {'rohit':"1234"}
    uname = input("enter username: ")
    password = input("enter password: ")

    if dict_.get(uname) == password:
        print("logged in ")
    else:
        print("invalid userid or password")
id_password()















