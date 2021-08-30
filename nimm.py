"""
Write a game starts with 20 stones 
between 2 players.
player can only take either 1 or 2 stones
Last player to take stone loses.
"""

import random

def main():
    stone_num = 20
    player = 1
    while stone_num > 0:
        stone_num = lets_play(stone_num, player)
        player = change_player(player)
        if stone_num == 0:
            print ("Player " +str(player)+" wins!")

def lets_play(stone_num, player):
    print ("There are " + str(stone_num) + " stones left")
    player_num = int(input("Player "+str(player)+" would you like to remove 1 or 2 stones? "))
    if player_num != 1 and player_num != 2:
        player_num = int(input("Please enter 1 or 2: "))
    stone_num -= player_num
    print()
    return stone_num

def change_player(player):
    if player == 1:
        player = 2
        return player
    if player == 2:
        player = 1
        return player


if __name__ == '__main__':
    main()
