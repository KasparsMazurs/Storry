# Interactive story

Interactive story is a Python terminal game.

In this game, players can choose how the story will play out.
In the story, payer can find 4 minigames:
 * Math - Players will be given 4 mathematical assignments.
 * Riddle - Players will be given three random riddles to solve
 * Math riddles - Players will be given 2 mathematical riddles 
 * Fighting - Players can try to win this minigame by reducing the opponent's health points.

## How to play

Playing this game players will be provided with choices of what to do. A player will need to type in his/her choices from the given one.

### Math minigame

To win the Math minigame you will need to solve 4 mathematical assignments by providing correct answer

### Riddle minigame

To win the Riddle minigame you will need to solve 2 riddles by providing correct answer

### Math riddles minigame

To win the Math riddles minigame you will need to solve 2 mathematical riddl assignments by providing correct answer

### Fighting minigame

To win Fighting minigame you will need to reduce computers health points before he do it to you. You will be able to aim your hits to head, body or legs and try to block hits to head, body or legs. And the computer will do the same. To win this game you will need to guest wear a computer will hit and try to block that place. And also try to guest wear computer will block and try to avoid being blocked. More unblocked hits you will make, the quicker will reduce computers health points. More hits you will guest and block the fewer health points you will lose.

## Features

### Existing Features

* Player's name that they will type at the start of the game always will appear with a capital letter, even if they will provide their name without it.
* All inputs in all games and mini-games are going through validation and error checks.

### Future Features

* Make story longer
* Create range of opponents in fighting minigame
* Create inventories that would help players in the game






## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!