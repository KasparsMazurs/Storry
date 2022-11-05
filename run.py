# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

name = input(f"Enter your name here \n").title()
print(f"----------------------------------\n")

def addition():
    """
    Here will be generated addition game
    """
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = a + b
    while True:
        answer = input(f'Can you solve this? \n {a} + {b} = ?\n')
        print(f"----------------------------------\n")
        # Check if answer is valid
        try:
            answer = int(answer)
        except:
            print(f"{name} can you count for me please till {answer}\n NO! \n Then, please provide me with number!\n")
            continue
        # Check if answer is correct
        if c == answer:
             print(f'Your right, answer was {answer}!\n')
             break
        else:
            print(f"That's wrong!\n")
            print(f"{name} think carefully!\n")

def subtraction():
    """
    Here will be generated subtraction game
    """
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    # Make sure that answer is a positive number
    if a < b:
        c = b - a
    else:
        c = a - b

    while True:
        if a < b:
            answer = input(f'Can you solve this? \n {b} - {a} = ?\n')
            print(f"----------------------------------\n")
            # Check if answer is valid
            try:
                answer = int(answer)
            except:
                print(f"{name} can you count for me please till {answer}\n NO! \n Then, please provide me with number!\n")
                continue
        else:
            answer = input(f'Can you solve this? \n {a} - {b} = ?\n')
            print(f"----------------------------------\n")
            # Check if answer is valid
            try:
                answer = int(answer)
            except:
                print(f"{name} can you count for me please till {answer}\n NO! \n Then, please provide me with number!\n")
                continue
        # Check if answer is correct
        if c == int(answer):
             print(f'Your right, answer was {answer}!\n')
             break
        else:
            print(f"That's wrong!\n")
            print(f"{name} think carefully!\n")

def multiplication():
    """
    Here will be generated multiplication game
    """
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = a * b
    while True:
        answer = input(f'Can you solve this? \n {a} * {b} = ?\n')
        print(f"----------------------------------\n")
        # Check if answer is valid
        try:
            answer = int(answer)
        except:
            print(f"{name} can you count for me please till {answer}\n NO! \n Then, please provide me with number!\n")
            continue
        # Check if answer is correct
        if c == answer:
             print(f'Your right, answer was {answer}!\n')
             break
        else:
            print(f"That's wrong!\n")
            print(f"{name} think carefully!\n")

def division():
    """
    Here will be generated division game
    """
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = a * b
    while True:
        answer = input(f'Can you solve this? \n {c} / {b} = ?\n')
        print(f"----------------------------------\n")
        # Check if answer is valid
        try:
            answer = int(answer)
        except:
            print(f"{name} can you count for me please till {answer}\n NO! \n Then, please provide me with number!\n")
            continue
        # Check if answer is correct
        if a == answer:
             print(f'Your right, answer was {answer}!\n')
             break
        else:
            print(f"That's wrong!\n")
            print(f"{name} think carefully!\n")

def math_minigame():
    """
    Here will be generated math mini-game
    """
    print(f"Ok {name}, let's start with something simple.\nI will check your skill to count. \n")
    addition()
    print(f"Good start {name}. let's try subtraction.\n")
    subtraction()
    print(f"Ohhh {name} your good at this. let's try multiplication.\n")
    multiplication()
    print(f"Impressive {name}, one last thing, let's check your division skills.\n")
    division()
    print(f"{name}, I will admit, I was wrong, your math skills are not bad at all.\n")

