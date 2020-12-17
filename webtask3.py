from webtask import website
def webdata(url):
    # sending url to website to create file with that website html code
    website(url)
    # filename from url dynamically
    filename = url.split(".")[1]+".html"
    # reading data from file
    with open(filename,'r') as filedata:
        # readline return data into list format to take actual data converting inti str form to split it
        freadlines=str(filedata.readlines())
        # spliting the data
        fdata=freadlines.split(",")
        #taking empty set
        set_=set()
        # taking each value and appending into set
        for value in fdata:
            if value.isdigit():
                set_.add(int(value))
        # print(set_)
        list_=list(set_)
        print(f"before: {set_}\n\n")
        # print(len(list_))
        newlist_=[]
        tuple_=()
        for value in list_:
            if value%2 == 0:
                # why dont we use discard here when i am using discard it is showing -->
                 # returning RuntimeError: Set changed size during iteration
                list_.remove(value)
            if value%3 == 0:
                list_.pop()
            if value%4 == 0:
                newlist_.append(value)

        print(f"after: {tuple(newlist_)}")
        # print(len(newlist_))
        # print(list_)
        # print(len(list_))





if __name__ == "__main__":
    url = "http://www.google.com"
    webdata(url)
    url = "http://www.amazon.com"
    webdata(url)
    url = "http://www.kfc.com"
    webdata(url)
    url = "http://www.colgate.com"
    webdata(url)
    url = 'http://www.gmail.com'
    webdata(url)
    url = 'http://stackoverflow.com'
    webdata(url)

