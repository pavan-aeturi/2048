# 2048
a simple 2048 game using python

We're using python alongside with pygame for GUI. We're implementing the 2048 game with a 2d matrix, upon which we added all the four moves and addition of random tile, all while tracking the score of player. We are also providing the player to take back his moves till 5 steps, player is also suggested the best possible next move for a given state, by calculating the max tile,list of all tiles and sum of all tiles possible in the next two steps. When there is no empty tile, the game ends.

In linux ubuntu distro:

make sure you have installed python3 and pip3

Download and browse to downloaded directory in terminal

commands:

  pip3 install pygame --upgrade

  python3 game.py
