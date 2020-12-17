from configparser import ConfigParser
user_data = {"David":"David@121",
                "john":"stepsy@$",
                "nova":"nancy"}
def authenticate():
    config = ConfigParser()
    config.read('config.ini')
    # if loggin success it will True else by default it's false
    success = False
    # to count the login atempts taken temp variable
    lcount = 0
    while True:
        # asking user to enter credentials
        uname = config.get('credentials1','uname')
        password = config.get('credentials1','password')

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
if __name__ == "__main__":
    authenticate()













