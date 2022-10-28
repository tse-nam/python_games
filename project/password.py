from ast import Pass

pwd = input("whats your master password? \n ")

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw=data.split("|")
            print("user:",user,"   |  password: ",passw)



def add():
    name=input("enter account name: ")
    password=input("enter the password: ")

    with open('password.txt','a') as f:
        f.write(name+"|"+password+"\n")



while True:
   
    mode =input("would you like to view or add new password or q ro quit? \n").lower()

    if mode=="q":
        quit()

    elif mode =="view":
        view()
        
    elif mode=="add":
        add()
      
    else:
        print("invalid mode")
        continue



