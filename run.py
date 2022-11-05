# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

def addition():
    """
    Here will be generated addition game
    """
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = a + b
    while True:
        answer = input(f'Can you solve this? \n {a} + {b} = ?\n')
        if c == int(answer):
             print(f'Your right, answer was {answer}!\n')
             break
        else:
            print(f"That's wrong!\n")
            print(f"Think carefully!\n")

addition()  