import time
from random import randint

responses = ["Yes", "No", "Possibly", "Ask again later", "IDK"]


def magic_eight_ball():
    print('What is your question?')
    question = input()
    print('Thinking...')
    time.sleep(3)
    print(responses[randint(0, 1)])
    end()


def end():
    print('Would you like to play again?')
    reply = input()
    if reply == 'Yes':
        magic_eight_ball()
    else:
        print('Thanks for playing!')


print("Welcome to Magic 8-Ball")
magic_eight_ball()
