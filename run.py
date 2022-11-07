# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

# print("Welcome to the interactive story where you can change directions of this story.")
# name = input(f"What will be the name of the main character?\n").title()
# print(f"----------------------------------\n")

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

def riddle_1():
    """
    Here will be generated 1 riddle for riddle mini-game.
    """
    while True:
        answer = input(f'What goes up but never comes back down?\n')
        print(f"----------------------------------\n")
        if answer == "age" or answer == "Age":
            print(f"Your right, answer is, {answer}!\n")
            break
        elif answer == "give up" or answer == "Give up":
            print(f"I am kinda disappointed in you {name}!\n")
            print(f"The answer was '{answer}'!\n")
            break
        elif answer == "Hint" or answer == "hint":
            print(f"This is directly connected with how old are you!\n")
        else:
            print(f"No that's not '{answer}'!\n")
            print(f"{name} think carefully!\n")
            print(f"And remember, you can always give up or ask for a hint. To do that you just say 'Hint' or 'Give up'!\n")

def riddle_2():
    """
    Here will be generated 2 riddle for riddle mini-game.
    """
    while True:
        answer = input(f'If you drop a yellow hat in the Red Sea, what does it become?\n')
        print(f"----------------------------------\n")
        if answer == "wet" or answer == "Wet":
            print(f"Your right, answer is '{answer}'!\n")
            break
        elif answer == "give up" or answer == "Give up":
            print(f"I am kinda disappointed in you {name}!\n")
            print(f"The answer was '{answer}'!\n")
            break
        elif answer == "Hint" or answer == "hint":
            print(f"That same will happen if you will drop your hat in the river or bath!\n")
        else:
            print(f"No that's not '{answer}'!\n")
            print(f"{name} think carefully!\n")
            print(f"And remember, you can always give up or ask for a hint. To do that you just say 'Hint' or 'Give up'!\n")

def riddle_3():
    """
    Here will be generated 3 riddle for riddle mini-game.
    """
    while True:
        answer = input(f"If you drop me, I'm sure to crack, but smile at me and I'll smile back. What am I?\n")
        print(f"----------------------------------\n")
        if answer == "mirror" or answer == "Mirror":
            print(f"Your right, answer is '{answer}'!\n")
            break
        elif answer == "give up" or answer == "Give up":
            print(f"I am kinda disappointed in you {name}!\n")
            print(f"The answer was '{answer}'!\n")
            break
        elif answer == "Hint" or answer == "hint":
            print(f"You use that when you what to see how you look!\n")
        else:
            print(f"No that's not '{answer}'!\n")
            print(f"{name} think carefully!\n")
            print(f"And remember, you can always give up or ask for a hint. To do that you just say 'Hint' or 'Give up'!\n")

def riddle_4():
    """
    Here will be generated 4 riddle for riddle mini-game.
    """
    while True:
        answer = input(f"What has hands and a face, but can't hold anything or smile?\n")
        print(f"----------------------------------\n")
        if answer == "clock" or answer == "Clock":
            print(f"Your right, answer is '{answer}'!\n")
            break
        elif answer == "give up" or answer == "Give up":
            print(f"I am kinda disappointed in you {name}!\n")
            print(f"The answer was '{answer}'!\n")
            break
        elif answer == "Hint" or answer == "hint":
            print(f"You look at this when you what to know what time it is!\n")
        else:
            print(f"No that's not '{answer}'!\n")
            print(f"{name} think carefully!\n")
            print(f"And remember, you can always give up or ask for a hint. To do that you just say 'Hint' or 'Give up'!\n")

def riddle_5():
    """
    Here will be generated 5 riddle for riddle mini-game.
    """
    while True:
        answer = input(f"You'll find me in Mercury, Earth, Mars and Jupiter, but not in Venus or Neptune. What am I?\n")
        print(f"----------------------------------\n")
        if answer == "r" or answer == "R":
            print(f"Your right, answer is '{answer}'!\n")
            break
        elif answer == "give up" or answer == "Give up":
            print(f"I am kinda disappointed in you {name}!\n")
            print(f"The answer was '{answer}'!\n")
            break
        elif answer == "Hint" or answer == "hint":
            print(f"It is something in the word!\n")
        else:
            print(f"No that's not '{answer}'!\n")
            print(f"{name} think carefully!\n")
            print(f"And remember, you can always give up or ask for a hint. To do that you just say 'Hint' or 'Give up'!\n")

def riddle_6():
    """
    Here will be generated 6 riddle for riddle mini-game.
    """
    while True:
        answer = input(f"I'm light as a feather, yet the strongest person can't hold me for five minutes. What am I?\n")
        print(f"----------------------------------\n")
        if answer == "breath" or answer == "Breath":
            print(f"Your right, answer is '{answer}'!\n")
            break
        elif answer == "give up" or answer == "Give up":
            print(f"I am kinda disappointed in you {name}!\n")
            print(f"The answer was '{answer}'!\n")
            break
        elif answer == "Hint" or answer == "hint":
            print(f"You do it all the time, and that's essential to live!\n")
        else:
            print(f"No that's not '{answer}'!\n")
            print(f"{name} think carefully!\n")
            print(f"And remember, you can always give up or ask for a hint. To do that you just say 'Hint' or 'Give up'!\n")

def riddle_7():
    """
    Here will be generated 7 riddle for riddle mini-game.
    """
    while True:
        answer = input(f"An elephant in Africa is called Lala. An elephant in Asia is called Lulu. What do you call an elephant in Antarctica?\n")
        print(f"----------------------------------\n")
        if answer == "lost" or answer == "Lost":
            print(f"Your right, answer is '{answer}'!\n")
            break
        elif answer == "give up" or answer == "Give up":
            print(f"I am kinda disappointed in you {name}!\n")
            print(f"The answer was '{answer}'!\n")
            break
        elif answer == "Hint" or answer == "hint":
            print(f"He is definitely not at home!\n")
        else:
            print(f"No that's not '{answer}'!\n")
            print(f"{name} think carefully!\n")
            print(f"And remember, you can always give up or ask for a hint. To do that you just say 'Hint' or 'Give up'!\n")

def riddle_8():
    """
    Here will be generated 8 riddle for riddle mini-game.
    """
    while True:
        answer = input(f"I jump when I walk and sit when I stand. What am I?\n")
        print(f"----------------------------------\n")
        if answer == "kangaroo" or answer == "Kangaroo":
            print(f"Your right, answer is '{answer}'!\n")
            break
        elif answer == "give up" or answer == "Give up":
            print(f"I am kinda disappointed in you {name}!\n")
            print(f"The answer was '{answer}'!\n")
            break
        elif answer == "Hint" or answer == "hint":
            print(f"It is an animal from Australia!\n")
        else:
            print(f"No that's not '{answer}'!\n")
            print(f"{name} think carefully!\n")
            print(f"And remember, you can always give up or ask for a hint. To do that you just say 'Hint' or 'Give up'!\n")

def riddle_9():
    """
    Here will be generated 9 riddle for riddle mini-game.
    """
    while True:
        answer = input(f"What do you get when you cross a snowman and a vampire?\n")
        print(f"----------------------------------\n")
        if answer == "frostbite" or answer == "Frostbite":
            print(f"Your right, answer is '{answer}'!\n")
            break
        elif answer == "give up" or answer == "Give up":
            print(f"I am kinda disappointed in you {name}!\n")
            print(f"The answer was '{answer}'!\n")
            break
        elif answer == "Hint" or answer == "hint":
            print(f"You can get that when you are cold outside!\n")
        else:
            print(f"No that's not '{answer}'!\n")
            print(f"{name} think carefully!\n")
            print(f"And remember, you can always give up or ask for a hint. To do that you just say 'Hint' or 'Give up'!\n")

def riddle_10():
    """
    Here will be generated 10 riddle for riddle mini-game.
    """
    while True:
        answer = input(f"What gets wet while drying?\n")
        print(f"----------------------------------\n")
        if answer == "towel" or answer == "Towel":
            print(f"Your right, answer is '{answer}'!\n")
            break
        elif answer == "give up" or answer == "Give up":
            print(f"I am kinda disappointed in you {name}!\n")
            print(f"The answer was '{answer}'!\n")
            break
        elif answer == "Hint" or answer == "hint":
            print(f"You use that after swimming or showering!\n")
        else:
            print(f"No that's not '{answer}'!\n")
            print(f"{name} think carefully!\n")
            print(f"And remember, you can always give up or ask for a hint. To do that you just say 'Hint' or 'Give up'!\n")

def riddle_11():
    """
    Here will be generated 11 riddle for riddle mini-game.
    """
    while True:
        answer = input(f"What has a head and a tail but no body?\n")
        print(f"----------------------------------\n")
        if answer == "coin" or answer == "Coin":
            print(f"Your right, answer is '{answer}'!\n")
            break
        elif answer == "give up" or answer == "Give up":
            print(f"I am kinda disappointed in you {name}!\n")
            print(f"The answer was '{answer}'!\n")
            break
        elif answer == "Hint" or answer == "hint":
            print(f"Usually, you can find that in wallet or piggy bank!\n")
        else:
            print(f"No that's not '{answer}'!\n")
            print(f"{name} think carefully!\n")
            print(f"And remember, you can always give up or ask for a hint. To do that you just say 'Hint' or 'Give up'!\n")

def riddle_minigame():
    """
    Here will be launched riddle mini-game
    """
    # generate 3 random numbers
    a = random.randint(1, 11)
    b = random.randint(1, 11)
    while b == a:
        b = random.randint(1, 11)
    c = random.randint(1, 11)
    while c == a or c == b:
        c = random.randint(1, 11)
    # sets up first riddle
    print(f"Ok {name}, here will be first riddle!\n")
    print(f"Riddle me this!\n")
    if a == 1:
        riddle_1()
    elif a == 2:
        riddle_2()
    elif a == 3:
        riddle_3()
    elif a == 4:
        riddle_4()
    elif a == 5:
        riddle_5()
    elif a == 6:
        riddle_6()
    elif a == 7:
        riddle_7()
    elif a == 8:
        riddle_8()
    elif a == 9:
        riddle_9()
    elif a == 10:
        riddle_10()
    else:
        riddle_11()
    print(f"Ok {name}, here will be second riddle!\n")
    print(f"Riddle me this!\n")
    if b == 1:
        riddle_1()
    elif b == 2:
        riddle_2()
    elif b == 3:
        riddle_3()
    elif b == 4:
        riddle_4()
    elif b == 5:
        riddle_5()
    elif b == 6:
        riddle_6()
    elif b == 7:
        riddle_7()
    elif b == 8:
        riddle_8()
    elif b == 9:
        riddle_9()
    elif b == 10:
        riddle_10()
    else:
        riddle_11()
    print(f"Ok {name}, here will be final riddle!\n")
    print(f"Riddle me this!\n")
    if c == 1:
        riddle_1()
    elif c == 2:
        riddle_2()
    elif c == 3:
        riddle_3()
    elif c == 4:
        riddle_4()
    elif c == 5:
        riddle_5()
    elif c == 6:
        riddle_6()
    elif c == 7:
        riddle_7()
    elif c == 8:
        riddle_8()
    elif c == 9:
        riddle_9()
    elif c == 10:
        riddle_10()
    else:
        riddle_11()
    print(f"Thank you {name}, I really enjoyed playing this with you.\n")

def hit_input_validation():
    """
    Here will be checked if hit input for fighting minigame is correctHere will be checked is input for fighting minigame is correct
    """
    while True:
        global hit
        hit = input(f"Where will you aim?\n")
        print(f"----------------------------------\n")
        # Check if answer is valid
        try:
            hit = int(hit)
        except:
            print(f" You typt {hit}, but you need to type 1, 2 or 3\n")
            continue
        if hit > 3 or hit < 1:
            print(f" You typt {hit}, but you need to type 1, 2 or 3\n")
            return hit_input_validation()
        else:
            break

def block_input_validation():
    """
    Here will be checked if block input for fighting minigame is correctHere will be checked is input for fighting minigame is correct
    """
    while True:
        global block
        block = input(f"What will you block?\n")
        print(f"----------------------------------\n")
        # Check if answer is valid
        try:
            block = int(block)
        except:
            print(f" You typt {block}, but you need to type 1, 2 or 3\n")
            continue
        if block > 3 or block < 1:
            print(f" You typt {block}, but you need to type 1, 2 or 3\n")
            return block_input_validation()
        else:
            break
    return block

def fight_minigame():
    """
    Here will be launched a fighting mini-game
    """
    HP = 100
    burglar = 100
    print(f"{name} health is: {HP}")
    print(f"Burglar health is: {burglar}\n")
    # This loop will go on while someone loses all health
    while True:
        if HP >= 0 and burglar >= 0:
            print("If you want to hit head type 1")
            print("If you want to hit body type 2")
            print(f"If you want to hit legs type 3\n")
            # Players hit input
            hit_input_validation()
            # Randomly generate burglars move
            burglar_block = random.randint(1, 3)
            # Checks damage to a burglar. If the burglar guesses correctly wear you were aiming burglar reves reduced damage
            if hit == burglar_block:
                a = random.randint(1, 10)
                burglar = burglar - a
                print(f"The burglar guests your move and manages to block your hit quite significantly.\n")
                print(f"{name} made damage to burglar: {a}")
                print(f"Burglars health is: {burglar}")
            else:
                c = random.randint(10, 30)
                burglar = burglar - c
                print(f"The burglar didn't guess where you will aim.\n")
                print(f"{name} made damage to burglar: {c}")
                print(f"Burglars health is: {burglar}")
            print(f"----------------------------------\n")
            print("If you want to block head type 1")
            print("If you want to block body type 2")
            print(f"If you want to block legs type 3\n")
            # Players block input
            block_input_validation()
            # Randomly generate burglars move
            burglar_hit = random.randint(1, 3)
            print(block)
            print(burglar_hit)
            # Checks damage to a player. If the player guesses correctly wear burglar will aiming player reves reduced damage.
            if burglar_hit == block:
                b = random.randint(1, 10)
                HP = HP - b
                print(f"{name} guest where the burglar will aim, so {name} received quite significantly less damage.\n")
                print(f"Burgler made damage to {name}: {b}")
                print(f"{name} health is: {HP}")
            else:
                d = random.randint(10, 20)
                HP = HP - d
                print(f"{name} guest wrong where the burglar will aim, so {name} received quite significant damage.\n")
                print(f"Burgler made damage to {name}: {d}")
                print(f"{name} health is: {HP}")
            print(f"----------------------------------\n")
            # Check if player wins game.
        else:
            if HP > 0:
                print(f"{name} win, burglar ran so fast away from {name} as he had never run before")
                print(f"After the burglar was war away {name} decided to get some rest, and get to sleep under a big fir tree")
            else:
                print(f"{name} lose, and was robbed")
                print(f"After the burglar was war away {name} decided to get some rest, and get to sleep under a big fir tree")
            break


def forrest():
    print("You chose river")

def raft():
    print("You chose river")

def river():
    print("You chose river")

def first_choice():
    

def main():
    while True:
        first_choice = input(f"first choice\n")
        if first_choice == "forrest":
            forrest()
        elif first_choice == "raft":
            raft()
        elif first_choice == "river":
            raft()
        else:
            print("try agen")
            return first_choice
        break
        ###################
    second_choice = input(f"second_choice\n")
    if second_choice == forrest:
        forrest()
    elif second_choice == raft:
        raft()
    elif second_choice == river:
        raft()
    else:
        print("try agen")
        return
        ####################
    third_choice = input(f"third_choice\n")
    if third_choice == forrest:
        forrest()
    elif third_choice == raft:
        raft()
    elif third_choice == river:
        raft()
    else:
        print("try agen")
        return
main()