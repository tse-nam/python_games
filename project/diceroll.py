
import random

def main():
    player1=0
    player2=0
    round=1
    player1_win=0
    player2_win=0


    while round!=4:
        print("round   :{} ".format(round))
        player1 = dice_roll()
        player2 = dice_roll()
        print("player1 rolled: {}".format(player1))
        print("player2 rolled: {}".format(player2))
        
        if player1==player2:
            print("draw!!!")

        elif player1>player2:
            print("player1 wins!!!")
            player2_win+=1
        else:
            print("player2 wins!!!")
            player2_win+=1
        round+=1
        

    if player1_win==player2_win:
        print("draw!!!")
            
    elif player1_win>player2_win:
        print("final winner player1 wins!!!")
          
    else:
        print("final winner player2 wins!!!")
            

def dice_roll():
    roll=random.randint(1,6)
    return roll

main()

