import random

class BaseGame:

    message_length = 60

    description = ""

    def __init__(self, points_to_win, n_lives=3):
        
        self.points_to_win = points_to_win
        
        self.points = 0
        
        self.lives = n_lives
    
    def get_numeric_input(self, message=""):

        while True:
            user_input = input(message)

            if user_input.isnumeric():
                return int(user_input)
            else:
                print("The input must be a number")
                continue
    
    def print_welcome_message(self):
        print("PYTHON MULTIPLICATION GAME".center(self.message_length))

    def print_lose_message(self):
        print("SORRY YOU LOST ALL OF YOUR LIVES".center(self.message_length))

    def print_win_message(self):
        print(f"CONGRATULATION YOU REACHED {self.points}".center(self.message_length))

    def print_current_lives(self):
        print(f"Currently you have {self.lives} lives\n")
    
    def print_current_score(self):
        print(f"\nYour score is {self.points}")
    
    def print_description(self):
        print("\n\n"+ self.description.center(self.message_length) + "\n")
    

    def run(self):
        self.print_welcome_message()

        self.print_description()

class RandomMultiplication(BaseGame):

    description = "In this game you must answer the random multiplication correctly\nYou win if you reach 5 points, or lose if you lose all your lives"

    def __init__(self):
        super().__init__(5)
    
    def get_random_numbers(self):

        first_number = random.randint(1, 10)
        second_number = random.randint(1, 10)

        return first_number, second_number
    
    def run(self):
        
        super().run()

        while self.lives > 0 and self.points_to_win > self.points:
            number1, number2 = self.get_random_numbers()

            operation = f"{number1} x {number2}: "

            user_answer = self.get_numeric_input(message=operation)
            
            if user_answer  == number1 * number2:
                print("\nYour answer is correct\n")

                self.points += 1
            
            else:
                print("\nSorry, your answer is incorrect\n")

                self.lives = -1

            
            self.print_current_score()
            self.print_current_lives()

        else:

            if self.points >= self.points_to_win:
                self.print_win_message()
            else:
                self.print_lose_message()

class TableMultiplication(BaseGame):
    def __init__(self):
         super().__init__(2)

    def run(self):

        super().run()

        while self.lives > 0 and self.points_to_win > self.points:
             
            number = random.randint(1, 10)

            for i in range(1, 11):

                if self.lives <= 0:

                    self.points = 0
                    break
                
                operation = f"{number} x {i}: "

                user_answer = self.get_numeric_input(message=operation)

                if user_answer == number * i:
                    print("Great! your answer is correct")
                else:
                     print("Sorry your answer isn't correct")

                     self.lives -= 1
                
                self.points += 1

        else:

            if self.points >= self.points_to_win:
                self.print_win_message()
            else:
                self.print_lose_message()

if __name__ == "__main__":
    
    print("Select Game mode")

    choice = input("[1], [2]: ")

    if choice == "1":
        game = RandomMultiplication()
    elif choice == "2":
        game = TableMultiplication()
    else:
        print("Please, select a valid game mode")
        exit()

    game.run()

