# I tried to learn using dict, list, random library in this program.
"""
You're going to play a simple werewolf game with my 5 instructors from CIP in this program.
There is only 1 werewolf, and the rest will be villagers.
You're the chief of this village.
To save your village, find the werewolf among them.
You'll lose if there is 1 name left (which means the werewolf is going to eat you)
"""
import random

PLAYER1 = "Mehran"
PLAYER2 = "Chris"
PLAYER3 = "Julie"
PLAYER4 = "Brahm"
PLAYER5 = "Lisa"


def main():
    welcome_to_play()
    ready = input ("Are you ready to play? (hit enter to stop): ")
    while True: 
        if ready == "":
            break
        character_dict = set_up_game()
        werewolf, villager_list = game_start(character_dict)
        play(werewolf, villager_list)
        ready = input ("Do you want to play another round? (hit enter to stop): ")



# print welcome sentences and let's the user know basic rules 
def welcome_to_play():
    print ("\nWelcome to play the simple werewolf game!\n")
    print ("You're going to play a game with 5 instructors from CIP in this program.")
    print ("There are only 1 werewolf, and the rest will be villagers.")
    print ("And you are the chief of this village.\n")
    print ("The werewolf will come at night and eat a villager.")
    print ("To save your village, find the werewolf among them.")
    print ("You'll lose if there is 1 name left (which means the werewolf is going to eat you!)\n")
    # ask if the user want to play now:
    #

"""
This is going to randomly choose 1 of 5 existing player as werewolf.
The rest of player will be villager.
"""
def set_up_game():
    werewolf = random.randint(1,5)
    if werewolf == 1:
        character_dict = {PLAYER1:'werewolf', PLAYER2:'villager',PLAYER3:'villager',PLAYER4:'villager',PLAYER5:'villager'}
        return character_dict
    if werewolf == 2:
        character_dict = {PLAYER1:'villager', PLAYER2:'werewolf',PLAYER3:'villager',PLAYER4:'villager',PLAYER5:'villager'}
        return character_dict
    if werewolf == 3:
        character_dict = {PLAYER1:'villager', PLAYER2:'villager',PLAYER3:'werewolf',PLAYER4:'villager',PLAYER5:'villager'}
        return character_dict
    if werewolf == 4:
        character_dict = {PLAYER1:'villager', PLAYER2:'villager',PLAYER3:'villager',PLAYER4:'werewolf',PLAYER5:'villager'}
        return character_dict
    if werewolf == 5:
        character_dict = {PLAYER1:'villager', PLAYER2:'villager',PLAYER3:'villager',PLAYER4:'villager',PLAYER5:'werewolf'}
        return character_dict

#ask if user is ready to play and print out the starting script of the game
def game_start(character_dict):
    print ("Our town now has 6 villagers: "+PLAYER1+", "+PLAYER2+", "+PLAYER3+", "+PLAYER4+", "+PLAYER5+" and you - the chief.")
    # this for loop to find out who is werewolf and create a villager list
    for key in character_dict.keys():
        character = character_dict.get(key)
        if character == "werewolf":
            werewolf = key
    character_dict.pop(werewolf)
    villager_list = list(character_dict.keys())
    return werewolf, villager_list


#the werewolf randomly choose a victim here, remove a player from the list based on random index
def get_werewolf_chose_victim(villager_list):
    print ("\nNight is falling in the village. Everyone is going to sleep.")
    print ("Werewolf, choose a victim for tonight's feast.")
    victim = villager_list.pop(random.randint(0,(len(villager_list)-1)))
    print ("Werewolf, close your eyes")
    return victim, villager_list


"""
user guess who is werewolf
If it's correct, print congratulations message
If it's wrong, keep remove a villager from the list
If it's out of turn, user is still get it wrong, print game over statement.
"""
def play(werewolf, villager_list):
    user_guess = "no one"
    while user_guess != werewolf :
        victim, villager_list = get_werewolf_chose_victim(villager_list)
        user_guess = input ("\nChief, who do you think is the werewolf: ")
        user_guess = is_guess_valid(user_guess)
        if user_guess == werewolf:
            print ("Congratulations! Your village has killed ", str(werewolf)," the werewolf, the town is safe now.")
            break
        if user_guess != werewolf and len(villager_list) == 0:
            print("\n",str(victim) + " were eaten in the night. Our village now has only you.")
            print("Oops",str(werewolf), " - the werewolf is going to eat you tonight! Game over!\n")
            break
        print_victim_info(victim, werewolf, villager_list)

#check if user type in the right name of players
def is_guess_valid(user_guess):
    while user_guess!=PLAYER1 and user_guess!=PLAYER2 and user_guess!=PLAYER3 and user_guess!=PLAYER4 and user_guess!=PLAYER5:
        user_guess = input("Please enter existing player: ")
    return user_guess

# print who were eaten in the night and how many people are still alive
def print_victim_info(victim, werewolf, villager_list):
    print("\n",str(victim) + " were eaten in the night. Our village now has you and:")
    villager_list.append(str(werewolf))
    print (random.sample(villager_list, len(villager_list)))
    villager_list.pop()


if __name__ == '__main__':
    main()
