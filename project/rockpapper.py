import random

user_win=0
computer_win=0

options=["rock","paper","scissor"]

while True:
    user_input=input("enter rock / paper / scissor / or q to quit     \n ").lower()
    if user_input == "q":

         break

    if user_input not in options:
         continue
    
    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print(options[random_number])
    
    if user_input=="rock" and computer_pick=="scissor":
        user_win+=1
        print("you win!!!")
    elif user_input=="paper" and computer_pick=="rock":
        user_win+=1
        print("you win!!!")
    elif user_input=="scissor" and computer_pick=="paper":
        user_win+=1
        print("you win!!!")

    else :
        print("computer wins!!!!")
        computer_win+=1

print("you win {} times and computer wins {} times".format(user_win,computer_win))
print("goood bye(*_*)")

 
