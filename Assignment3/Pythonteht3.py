from urllib.request import urlopen

while (True):
    try:
        
        url = input("Enter URL: ")
        if not url: break
        content = urlopen(url)
        path = input("enter path: ")
        saveFile = open(path,'w')
        saveFile.write(str(content.read()))
        saveFile.close()
        print("Content saved")
        break
    except:
        print("Cant open URL, try again")
        continue
        
