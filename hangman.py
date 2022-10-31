import random
from re import A
import string
words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                   ,"plants"]



def get_word():
    return random.choice(words_to_guess)

def hangman():
    word=get_word().upper()
    print (word)
    word_letter=set(word)
    apl=set(string.ascii_uppercase)
    used_words=set()
    


    lives=6 

    while len(word_letter) > 0 and  lives > 0:
        print("used letters"," ".join(used_words))
        word_list=[letter if letter in used_words else " _ " for letter in word]
        print("currnt word list:","_".join(word_list))

        user_word=input("guess a letter \n").upper()
        
    
        if user_word in apl - used_words:
            used_words.add(user_word)
            if user_word in word_letter:
                word_letter.remove(user_word)
            else:
                lives=lives-1
                print("lives : {}".format(lives))
        elif user_word in used_words: 
            print("you used the letter:")
        
        else:
           print("invald")
    
    if lives==0:
        print("you loose and the word is {}".format(word))
    else :
        print (" you win and the word is {}".format(word))
        
       

hangman()







 