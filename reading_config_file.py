from configparser import ConfigParser


def readconfig():

    parser = ConfigParser()
    parser.read('config.ini')

    print(parser.sections())
    print(parser.get('credentials','uname'))
    print(parser.get('credentials','password'))
    print(parser.get('credentials1','uname'))
    print(parser.get('credentials1','password'))
    print(parser.options('settings'))

    # check the db section available or not
    print("db" in parser)
    # we can check the type
    print(parser.get('db','db_port'),type(parser.get('db','db_port')))
if __name__ == "__main__":
    readconfig()
