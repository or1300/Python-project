import MemoryGame
import GuessGame
import CurrencyRouletteGame
import Score


def welcome(name):
    return "\nHello" + name + " and welcome to the world of Games (WoG). \nHere you can findmany cool games to play\n"


def load_game():
    global result
    no_exception = False
    while no_exception == False:
        print("Please choose a game to play: \n"
              "\t1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n"
              "\t2. Guess Game - guess a number and see if you chose like the computer \n"
              "\t3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
        try:
            user_game_choice = int(input(">>>"))
            if user_game_choice not in range(1, 4):
                raise ValueError
            else:
                no_exception = True
        except ValueError as e:
            print("!!! Numbers 1, 2, 3 are only !!!")

    no_exception = False
    while no_exception == False:
        print("Please choose game difficulty from 1 to 5:")
        try:
            user_dificulty_choice = int(input(">>>"))
            if user_dificulty_choice not in range(1, 6):
                raise ValueError
            else:
                no_exception = True
        except ValueError as e:
            print("!!! Numbers from 1 to 5 are only !!!")

    if user_game_choice == 2:
        GuessGame.set_difficulty(user_dificulty_choice)
        result = GuessGame.play()
    elif user_game_choice == 1:
        MemoryGame.set_difficulty(user_dificulty_choice)
        result = MemoryGame.play()
    elif user_game_choice == 3:
        CurrencyRouletteGame.set_difficulty(user_dificulty_choice)
        result = CurrencyRouletteGame.play()

    if result == True:
        print("                                     You won")
        Score.add_score(user_dificulty_choice)
    else:
        print("                                     You lost")
        Score.create_zero_score()
