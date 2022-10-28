from curses.ascii import isdigit
import random

r=random.randrange(11)
print(r)
 
while True:
    guess=input("guess the number \n")
    if guess.isdigit():
        guess=int(guess)
    else:
        print("enter number again!!")
        continue
    if guess!=r:
        print("you guess the incorrect number")
        continue
    else:
        print("you guess the correct number(*_*)")

        



