import random
from time import sleep
from Utils import Screen_cleaner

difficulty = 3
list = []

def generate_sequence():
    global list
    for index in range(0, difficulty):
        list.append(random.randint(1, 100))

def get_list_from_user():
    guess_list = []
    for index in range(1, difficulty + 1):
        no_exception = False
        while no_exception == False:
            print("Please type your guess number by number - " + str(index) +  " number: ")
            try:
             user_guess = int(input(">>>"))
             if (user_guess) not in range(1, 101):
                 raise  ValueError
             else:
                 no_exception = True
            except ValueError as e:
             print("!!! Numbers between 1 to 100 are only !!!")
        guess_list.append(user_guess)
    return guess_list

def is_list_equal():
    list1 = set(list)
    print("You chose memory Game. Try to memorize the following set of numbers: ")
    print(list1)
    sleep(0.9)
    print("\n"*100)
    Screen_cleaner()
    list2 = set(get_list_from_user())
    print("System casted numbers: " + str(list1) +", you entered numbers : " + str(list2) + "." )
    if len(list1 & list2) == difficulty:
        return True
    return False

def play():
    generate_sequence()
    return is_list_equal()

def set_difficulty(difficulty_value):
    global difficulty
    difficulty = difficulty_value
