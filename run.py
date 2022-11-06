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

def addition_riddle():
    """
    Here will be generated addition riddle game
    """
    # Generate some random fruit for game
    fruit_list = ['apples', 'oranges', 'bananas', 'lemons', 'watermelons', 'mangoes', 'peaches']
    secure_random = random.SystemRandom()
    fruit1 = secure_random.choice(fruit_list)
    fruit2 = secure_random.choice(fruit_list)
    # Generate numbers for game 
    a = random.randint(2, 20)
    b = random.randint(2, 20)
    c = a - 1 + b - 1 
    # Generate riddle
    while True:
        print(f"Tom has {a} {fruit1} , one of them was spoiled, so he threw it away and put into the bowl all {fruit1} which wast spoiled,\nbut Tom's brother has {b} {fruit2}. \nTom's brother eats one and all other {fruit2} put into the bowl. \n")
        answer = input(f'How many fruits are in the bowl?\n')
        print(f"----------------------------------\n")
        try:
            answer = int(answer)
        except:
            print(f"{name} I can give you a hint, it's not {answer}, answer should be a number\n")
            continue
        # Check if answer is correct
        if c == answer:
             print(f'Your right, answer was {answer}!\n')
             break
        else:
            print(f"No! That's not correct!\n")
            print(f"{name} read riddle carefully!\n")

def division_riddle():
    """
    Here will be generated division riddle game
    """
    # Generate some random vegetables for the game and make sure that there will be three various vegetables 
    vegetables_list = ['spinaches', 'carrots', 'broccolis', 'brussels sprouts', 'kales', 'green peas', 'beets']
    secure_random = random.SystemRandom()
    vegetable1 = secure_random.choice(vegetables_list)
    vegetable2 = secure_random.choice(vegetables_list)
    while vegetable2 == vegetable1:
        vegetable2 = secure_random.choice(vegetables_list)
    vegetable3 = secure_random.choice(vegetables_list)
    while vegetable3 == vegetable2 or vegetable3 == vegetable1:
        vegetable3 = secure_random.choice(vegetables_list)
    # Generate numbers for game 
    a = random.randint(2, 10)
    b = 2 * (random.randint(2, 10))
    c = 2 * (random.randint(2, 10))
    d = a + (b + c)/2
    # Generate riddle
    while True:
        print(f"Jack's mom gets 3 bags of vegetables from the town.\nIn the first bag there was {a} {vegetable1}.\nIn the second bag there was {b} {vegetable2}.\nIn the third  bag there was {c} {vegetable3}.\nWhen she gets home she realizes she doesn't need so many vegetables, so she decides to give some vegetables to her neighbor.\nShe gives to neighbor half of {vegetable2} and {vegetable3}.\nWith how many vegetables are Jack's mom left?  ")
        answer = input(f'How many fruits are in the bowl?\n')
        print(f"----------------------------------\n")
        try:
            answer = int(answer)
        except:
            print(f"{name} I can give you a hint, it's not {answer}, answer should be a number\n")
            continue
        # Check if answer is correct
        if d == answer:
             print(f'Your right, answer was {answer}!\n')
             break
        else:
            print(f"No! That's not correct!\n")
            print(f"{name} read riddle carefully!\n")    

def math_riddle_minigame():
    """
    Here will be generated math riddle mini-game
    """
    print(f"{name}, Let's start with a simple math riddle\n")
    addition_riddle()
    print(f"Ok {name}, let's go forward, you will need more to impress me!\n")
    division_riddle()
    print(f"Now you impress me, you have great skills!")
