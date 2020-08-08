class GuessGame:
    def __init__(self, number, mn=0, mx=100):
        self.number = number
        self.guesses = 0
        self.min = mn
        self.max = mx

    def get_guess(self):
        guess = input(f"Please guess a number between {self.min} @ {self.max}: ")
        if self.valid_number(guess):
            return int(guess)
        else:
            print("We need an Integer value, try again.")
            return self.get_guess()

    def valid_number(self, str_guess_number):
        pass
