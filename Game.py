from words import Word
import random

class Game(Word):

    hidden_list = []
    display_list = []

    def __init__(self, attempts=5, hints=3):
        super().__init__()
        self.attempts = attempts
        self.hints = hints
        self.display_list.clear()
        self.hidden_list.clear()
        word = self.game_word
        for letter in word:
            self.hidden_list.append(letter)
            self.display_list.append('_')

    def show(self):
        return ' '.join(self.display_list)

    def getword(self):
        return self.game_word

    def reveal(self, indexlist):
        for index in indexlist:
            self.display_list[index] = self.hidden_list[index]
        return self.show()

    def reveal_hint(self):
        #Find all the indexes of '_'
        indexList = [i for i,x in enumerate(self.display_list) if x == '_']
        #Select one of the indexes from indexList (to reveal)
        index = random.choice(indexList)

        #change the element in that index from '_' to the actual letter
        self.display_list[index] = self.hidden_list[index]

        #Clear thing list or else next time when you get index lis again it will append to existing values
        indexList.clear()
        return self.show()

    def play(self):

        while True:

            # Let him Guess a letter
            guess = input('({} Attmepts left)Your guess: '.format(self.attempts))
            self.attempts -= 1
            if guess.upper() == 'QUIT':
                break
            elif guess.upper() == 'HINT':
                if not self.hints > 0:
                    print('No more hints left!')
                    print(' '.join(self.display_list))
                    continue
                self.hints -= 1
                self.attempts += 1
                self.reveal_hint()

            # Get the indexes of the matches
            indexesList = [i for i in range(len(self.getword())) if self.getword().startswith(guess, i)]

            # Reveal all the letters matched
            new_display = self.reveal(indexesList)
            indexesList.clear()

            # Print new display after revealing letters
            print(new_display)

            # Check if any letters are left to be solved, if not print output
            if '_' not in self.display_list:
                print('Yay, You got all the letters!')
                break
            # Check to see if attempts are left
            if self.attempts <= 0:
                print('Uh oh you used up all your attempts! Better luck next time.')
                break






