import csv
import re

def is_empty(fin):
    with open(fin) as file:
        r=file.read() 
        if (len(r)==0):
            return True
        else:
            return False
        
def edittor(fin,field,anum,replace):
    heading=["user","pin","acc_number","balance"]
    lstr = []
    with open (fin) as file:
        data = file.readlines() #list of strings  [", , , ",", , , ,",]
        for i in data:
            l=i.split(",") #list of strings
            if (l[2] == str(anum)):
                ind = heading.index(field)
                l[ind] = str(replace) + "\n"  #["","","",""]
                s=",".join(l) 
                lstr.append(s)
            else:
                lstr.append(i)
    with open (fin,"w") as file:
        file.writelines(lstr)
        print("Done!")
            
def acc_read(fin,anum):
    with open(fin) as file:
        cur=csv.DictReader(file)
        for row in cur:
            if (row["acc_number"] == str(anum)):
                return (row)
            
def withdraw(fin,anum,amt):
    data_dict = acc_read(fin,anum)
    nbal = int(data_dict["balance"])-amt
    edittor(fin,"balance",anum,nbal)

def transfer(fin,acc_from,acc_to,amt):
    with open (fin) as file:
        l_from = acc_read(fin,acc_from)
        l_to = acc_read(fin,acc_to)
        x_from = int(l_from["balance"])-amt
        x_to = int(l_to["balance"]) + amt
        edittor(fin,"balance",acc_from,x_from)
        edittor(fin,"balance",acc_to,x_to)

print("<<<Hello and welcome to THE GREAT BANK>>>")
global_anum=0
z = int(input("To create new account press 1, To login into your account press 2:\n"))
if z == 1:
    User_Name = input("What is your User Name?\n ")
    while (True):
        pin = int(input("Enter the pin:\n"))
        if (len(str(pin))<4):
            print("Pin is short, Enter the pin again.")
            continue
        else:
            False
            break
    acc_number = int(input("Enter the acc number:\n"))
    if re.search(r"^[0-9]", str(acc_number)):
        print("Valid acc_number")
        global_anum = acc_number
    else:
        print("Invalid acc_number")
    balance = int(input("Deposit amount in your account\n"))
    if (balance<5000):
        print("Not enough money!")
    else:
        print("Account has been successfully created!")
    user = {"user":User_Name,"pin":pin,"acc_number":acc_number,"balance":balance}
    with open("user.csv","a",newline="") as file:
        fieldname=["user","pin","acc_number","balance"]
        cur = csv.DictWriter(file,fieldnames=fieldname)
        if (is_empty("user.csv") is True):
            cur.writeheader()
            cur.writerow(user)
        else:
            cur.writerow(user)
            print()
elif z== 2:
    anum=int(input("Enter your account number: "))
    global_anum = anum
    data_lst = acc_read("user.csv",anum)
    if data_lst["acc_number"] == str(anum):
        lin = input("Enter your user name: ")
        pin = input("Enter your pin: ")
        if data_lst["pin"] == pin:
            print("Hello User")
y = True
while (y == True):
    x = int(input("For Checking Balnce press 0.\nFor Withdrawing press 1.\nFor Depositing money in your account press 2.\nFor Transferring money to another account press 3.\n"))
    try:
        if x == 0:   
            data = acc_read("user.csv",global_anum)
            print("Your Current Balance is: ",data["balance"])
        elif x == 1:
            amt = int(input("Enter the amount to be withdrawed.\n"))
            withdraw("user.csv", global_anum, amt)
            print(f"{amt} has been successfully withdrawed.")
        elif x == 2:
            amt = int(input(" Enter the amount to be deposited:\n"))
            withdraw("user.csv", global_anum, 0-amt) # -amt from withdraw
            print(f"{amt} has been successfully deposited.")
        elif x == 3:
            to = (input("Enter the account number of the person whom you want to transfer the money:\n "))
            amt = int(input("Enter the amount to be transferred:\n"))
            transfer("user.csv", global_anum, to, amt )
            print(f"{amt} has been succesfully transfer to account number {to}")
        y = input("Wanna continue? y/n:\n")
        if y == "y" :
            print()
            y = True
        else:
            print("Please come again.")
            y = False
    except:
        print("Account not found")
        y = input("Wanna continue? y/n:\n")
        if y == "y" :
            print()
            y = True
        else:
            print("Please come again.")
            y = False
            
        