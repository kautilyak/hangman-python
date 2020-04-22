from player import Player
from Game import Game

# create instance of player class with name
p1 = Player()

def start_game():
    #create a Game round and automatically select the word
    round = Game()
    #Show the user hidden version of the word
    print(round.show())
    #play the game
    round.play()

#Start the game
start_game()

#Check to see if he wants to play again
while True:
    replay = input('Do you wanna play one more? (Y/N)')
    if replay.upper() == "Y":
        start_game()
    elif replay.upper() == "N":
        print('Thanks for playing, {}!'.format(p1.name))
        break

