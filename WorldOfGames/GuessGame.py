import random

difficulty = 3
secret_number = 0

def generate_number():
    global secret_number
    secret_number = random.randint(1, difficulty)

def get_guess_from_user():
    no_exception = False
    while no_exception == False:
        print("You chose Guess Game. The system randomly casted number between 1 and " + str(difficulty) +
              ". \nPlease type your guess (Number between 1 and " + str(difficulty) + "): ")
        try:
            user_guess = input(">>>")
            if int(user_guess) not in range(1, difficulty+1):
                raise ValueError
            else:
                no_exception = True
        except ValueError as e:
            print("!!! Numbers between 1 to diffuculty are only !!! ")
    return int (user_guess)

def compare_results():
    guess_from_user = get_guess_from_user()
    print("System casted number " + str(secret_number) + ", you entered number " + str(guess_from_user) + ".")
    return secret_number == guess_from_user

def play():
    generate_number()
    return compare_results()

def set_difficulty(difficulty_value):
    global difficulty
    difficulty = difficulty_value