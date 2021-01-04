import re

while True:
    PID = input("Give a PID: ")
    if re.match(r"^(0[1-9]|[12]\d|3[01])(0[1-9]|1[0-2])([5-9]\d\+|\d\d-|[01]\dA)\d{3}[\dABCDEFHJKLMNPRSTUVWXY]$", PID):
        gender = int(PID[7:10])
        checksum = PID[0:6]+PID[7:10]
        year = ""
        if PID[6] == "-" :
            year = ".19"
        if PID[6] == "A" :
            year = ".20"
        bday= PID[0:2] + "." + PID[2:4] + year + PID[4:6]
        DICT= {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15, "H":16, "J":17, "K":18, "L":19, "M":20, "N":21, "P":22, "R":23, "S":24, "T":25, "U":26, "V":27, "W":28, "X":29, "Y":30}
        try:
            if int(PID[-1]) is int(checksum)%31:
                print("Checksum is valid!")
            else:
                print("Checksum is invalid!")
                break
        except ValueError:
            if DICT[(PID[-1])] is not int(checksum)%31:
                print("Checksum is invalid!")
                break
            else:
                print("Checksum is valid!")
        if (gender%2==0):
            print ("You are a female and you have a valid finnish id! Your birthday is "+bday+".")
            break  
        else:
            print ("You are a male and you have a valid finnish id! Your birthday is "+bday+".")
            break
    else:
        print ("Could not read id")