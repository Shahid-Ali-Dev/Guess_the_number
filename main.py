import random
logo = r'''
  ____  __ __    ___  _____ _____     ______  __ __    ___          ____   __ __  ___ ___  ____     ___  ____  
 /    ||  |  |  /  _]/ ___// ___/    |      ||  |  |  /  _]        |    \ |  |  ||   |   ||    \   /  _]|    \ 
|   __||  |  | /  [_(   \_(   \_     |      ||  |  | /  [_         |  _  ||  |  || _   _ ||  o  ) /  [_ |  D  )
|  |  ||  |  ||    _]\__  |\__  |    |_|  |_||  _  ||    _]        |  |  ||  |  ||  \_/  ||     ||    _]|    / 
|  |_ ||  :  ||   [_ /  \ |/  \ |      |  |  |  |  ||   [_         |  |  ||  :  ||   |   ||  O  ||   [_ |    \ 
|     ||     ||     |\    |\    |      |  |  |  |  ||     |        |  |  ||     ||   |   ||     ||     ||  .  \
|___,_| \__,_||_____| \___| \___|      |__|  |__|__||_____|        |__|__| \__,_||___|___||_____||_____||__|\_|
                                                                                                               
'''
def game(life, number):
    """Main function to start guessing the numbers"""
    print(f"You have a total of {life} attempts in this mode, Good Luck.")
    print("Choose a number between 1 to 100")
    while life != 0:
        try:
            guess = int(input("Make your guess. "))
            if guess == number:
                print(f"Yes the number is indeed {number}\nCongratulations on winning this game.")
                break
            elif guess > number:
                print("Go Lower")
            elif guess < number:
                print("Go Higher")
            life -= 1
            print(f"Your remaining attempts: {life}")
        except ValueError:
            print("Type a valid number")
    if life == 0:
        print(f"Sorry you lost the game, the number was {number}")
def run():
    """To ask the user if they want to play the game again or not"""
    ask = input("Would you like to play the game again? Type 'y' for yes or 'n' for no.\n").lower()
    if ask == "y":
        print("\n"*20)
        difficulty()

def difficulty():
    """We can choose the game difficulty"""
    print(logo)
    print("Welcome to the Number guessing game.")
    number = random.randint(1, 100)
    choose = input("Choose a difficulty. Type 'easy' or 'hard'.\n").lower()
    if choose == "easy":
        game(10, number)
        run()
    elif choose == "hard":
        game(5, number)
        run()
    else:
        print("Invalid inputs, Try again")
        run()
difficulty()