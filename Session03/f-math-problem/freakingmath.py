from random import *

def generate_quiz():
    x = randint(1, 10)
    y = randint(1, 10)
    # Hint: Return [x, y, op, result]
    return [3, 7, '+', 10]

def check_answer(x, y, op, display_result, user_choice):
    result = calc(x, y, op)
    if result == display_result:
        if user_choice == True:
            return True
        else:
            return False
        else:
            if user_choice == True:
                return False
            else:
                return True
    
