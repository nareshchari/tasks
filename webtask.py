import requests

def website(url):
    url_ = requests.get(url)
    if url_.status_code == 200:
        data = url_.text
        if type(data) == str:
            filename = url.split(".")[1]+".html"
            with open(filename,'w+') as filenew:
                filenew.write(data)
        else:
            print("something went wrong please try again")
    else:
        print(f"{url_.status_code}")


if __name__ == '__main__':
    # url='http://www.instagram.com'
    url='http://www.google.com'
    website(url)
