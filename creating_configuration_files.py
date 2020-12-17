"""here creating configuration file and definig some configurations"""
"""pip install configparser"""
import configparser

def writeconfig():

    config = configparser.ConfigParser()
    config['credentials'] = {
        'uname': 'XXXXXXX',
        'password': 'XXXXXXXX'
    }

    config['credentials1'] = {
        'uname': 'David',
        'password': 'David@121'
    }

    config['settings'] = {
        'debug': 'true',
        'secreat_key': 'abc123',
        'log_path': '/my_app/log'
    }

    config['db'] = {
        'db_name': 'myapp_dev',
        'db_host': 'localhost',
        'db_port': '8889'
    }

    config['files'] = {
        'use_cdn': 'false',
        'images_path': '/my_app/images'
    }

    with open('config.ini','w') as conf:
        config.write(conf)

if __name__ == "__main__":
    writeconfig()



# here it prints the configparser object name
# print(config)
# it is not printing the values of the key
# for k,v in config.items():
#     print(k,v)





























# def sum_two_iterables():
#     values = set(input('enter numbers: ').split(' '))#list of values
#     print(values)
#     total = 0
#     for i in values:
#         total += int(i)
#     print(total)



#     # li = []
#     # print(set1)#printing numbers
#     # set2 = set()#set2={1,2,3}
#     # for j in set1:
#     #     li.append(int(j))
#     #     total = 0
#     #     for i in a:
#     #         total += i
#     # print(total)
#     # print(set(li))


# if __name__ == '__main__':
#     sum_two_iterables()
