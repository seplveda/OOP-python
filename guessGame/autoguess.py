from guessgameOOP import GuessGame
import random

class Experimentum(GuessGame):

    def get_random_guess(self):
        guess = random.randint(self.min, self.max)
        if self.valid_number(guess):
            return int(guess)
        else:
            print("We need an Integer value, try again.")
            return self.get_guess()

    def play(self):
        self.guesses = 0
        # To Do: make more flexible for test algorithms
        self.min = 0
        self.max = 100
        while True:
            self.guesses += 1

            guess = self.get_random_guess()

            if guess < self.number:
                #self.min = guess
                pass
            elif guess > self.number:
                #self.max = guess
                pass
            else:
                break

        return 1/self.guesses