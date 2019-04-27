"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

 Extra information gathered from the following sites:

 1. Tuple information :   https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/
 2. Comparison to None :  https://docs.quantifiedcode.com/python-anti-patterns/readability/comparison_to_none.html
 3. Center method :       https://www.programiz.com/python-programming/methods/string/center

"""

import random
import os

border = ('═' * 50)
border2 = ('█' * 50)


def INVALID_OPTION():
    print('Please enter a valid entery.\n')
    input('Press [Enter] to continue...')

def CLEAR():
    os.system('clear' if os.name == 'posix' else 'cls')

def START_GAME():
    game_running = True
    high_score = None 
    high_score_player = "Charlie"
    while game_running:
        title_looping = True
        while title_looping:
            try:
                CLEAR()
                print(border)
                print('Number Guessing Game!'.center(50))
                print('by Carlos A. Marin'.center(50))
                print(border)
                print('\n\n')
                print(border2)
                print('█ 1. Play Game  █ 2. #1 player!  █ 3. Quit Game  █'.center(50))
                print(border2)
                selection = int(input('\n\nEnter one of the corresponding numbers: '))
            except ValueError:
                CLEAR()
                INVALID_OPTION()
                continue
            else:
                if selection == 1:    #Play Game
                    replay, high_score, high_score_player = game(high_score, high_score_player) # This function processes 3 variables. Types by order: [boolean, high_score value, high_score_player value]
                    if replay == True:
                        continue 
                    elif replay == False:# end-game
                        game_running = False
                        champion(high_score, high_score_player)
                        break
                elif selection == 2: #1 Player
                    menu_high_score(high_score, high_score_player)
                elif selection == 3: # Quit
                    asking_to_quit = True
                    while asking_to_quit:
                        CLEAR()
                        quitting = menu_end_game()
                        if quitting == True: 
                            champion(high_score, high_score_player)
                            game_running = False 
                            title_looping = False
                            break
                        elif quitting == False:
                            break
                elif selection not in range(1,4): #invalid option.
                    CLEAR()
                    INVALID_OPTION()
                    CLEAR()

def game(high_score, high_score_player):
    answer = random.randint(1, 10)
    score = 0
    CLEAR()
    print('\n\n')
    print(border)
    player = input('Enter player name: ')
    CLEAR()
    if high_score == None:
        print('\nWelcome, {}!'.format(player))
        print(border)
        print('\nA random number from 1-10 has been randomly selected.')
        print('For every guess, your score points will add up.')
        print('Try to guess the random number with the least amount ')
        print('of guesses in order to claim 1st place!\n')
        print('There are no previous plays therefore no high score has been set.\n')
        print('Enjoy!\n')
        input('Press [Enter] to continue...')
    else:
        print('\nWelcome, {}!'.format(player))
        print(border)
        print('\nA random number from 1-10 has been randomly selected.')
        print('For every guess, your score points will add up.')
        print('Try to guess the random number with the least amount ')
        print('of guesses in order to claim 1st place!\n')
        print('1st place is currently held by {}, with the score of "{}"\n'.format(high_score_player, high_score))
        print('Enjoy!\n')
        input('Press [Enter] to continue...')
    CLEAR()
    game_looping = True
    while game_looping:
        try:
            if high_score == None:
                print(border)
                print('Player: {}  |  Score: {}'.format(player, score).center(50))
                print(border)
                print('\n')
                print(border2)
                print('█' + 'High Score: None'.center(48) + '█')
                print(border2)
                print('\n')
                guess = int(input('Guess a number between 1-10: '))
            else:
                print(border)
                print('Player: {}  |  Score: {}'.format(player, score).center(50))
                print(border)
                print('\n')
                champion = ('█' + 'The current high score: "{}" by player: "{}"'.format(high_score, high_score_player).center(48) + '█')
                print('█' * len(champion)) #Special border - auto adjust size
                print(champion)
                print('█' * len(champion)) #special border - auto adjust size
                print('\n')
                guess = int(input('Guess a number between 1-10: '))
            score += 1
            CLEAR()
            if guess not in range(1, 11):
                CLEAR()
                print('\nYou must guess in the range of 1-10.\n')
                input('Press [Enter] to continue...')
                CLEAR()
            elif guess > answer:
                CLEAR()
                print('\nYour guess of "{}" is greater than the random number.\n'.format(guess))
                input('Press [Enter] to continue...')
                CLEAR()
            elif guess < answer:
                CLEAR()
                print('\nYour guess of "{}" is less than the random number.\n'.format(guess))
                input('Press [Enter] to continue...')
                CLEAR()
            elif guess == answer:
                high_score, high_score_player = check_high_score(score, high_score, player, high_score_player) # determine if current game surpasses previous scores
                playing_boolean = final_end_game() # determine if player wishes to continue
                return playing_boolean, high_score, high_score_player
        except ValueError:
            CLEAR()
            INVALID_OPTION()
            CLEAR()
    
        
#=========================================================================================================================================

    #Menu option 2
def menu_high_score(high_score, high_score_player): 
    CLEAR()
    if high_score == None:
        print(border)
        print('\nThere are no scores posted...\n')
        print(border)
        input('\npress [Enter] to continue...')
    else:
        print(border)
        print('\n{} is the champion with the score of "{}"\n'.format(high_score_player, high_score))
        print(border)
        print('\n')
        input('Press [Enter] to continue...')
        CLEAR()

    #Menu option 3
def menu_end_game(): 
    while True:
        CLEAR()
        print('Are you sure you want to quit?')
        quitting = input('All data will be lost! ([Y]es/[N]o): ').upper()
        if quitting == 'Y' or quitting == 'YES':
            return True
        elif quitting == 'N' or quitting == 'NO':
            return False
        else:
            CLEAR()
            INVALID_OPTION()
            continue
            
            

    #determines high_score and, high_score_player.
def check_high_score(score, high_score, player, high_score_player): 
    CLEAR()
    print('\nYou\'ve guessed the correct number!')
    print('Your score is "{}"\n\n'.format(score))
    print(border)
    if high_score == None:
        high_score = score 
        high_score_player = player
        print('The new high score is: "{}" by the player "{}"\n'.format(high_score, high_score_player))
        input('Press [Enter] to continue...')
    elif score <= high_score:
        CLEAR()
        print('Congratulations, {}! You hold 1st place!\n'.format(player))
        print('The previous high score is: "{}" by the player "{}"'.format(high_score, high_score_player))
        print(border)
        print('\n Your score is: "{}"'.format(score).center(50))
        input('\nPress [Enter] to continue...')
        high_score = score
        high_score_player = player
    else:
        print('Sorry, but your score of "{}" does not surpass the score of "{}" by the player "{}"\n'.format(score, high_score, high_score_player))
        print(border)
        input('\nPress [Enter] to continue...')
    return high_score, high_score_player

    #Asking for a replay
def final_end_game():
        loopy = True
        while loopy:
            CLEAR()
            print('Would you like a replay?')
            final_break = input('All data will be lost once game session is ended. ([Y]es/[N]o): ').upper()
            if final_break == 'Y' or final_break == 'YES':
                return True
            elif final_break == 'N' or final_break == 'NO':
                return False
            else:
                CLEAR()
                print('Please enter a valid entery.\n')
                input('Press [Enter] to continue...')
                continue
                
    #Shows Winner at end of game.         
def champion(high_score, high_score_player):
    CLEAR()
    if high_score == None:
        pass
    else:
        print(border.center(150))
        print('The Champion is....\n'.center(150))
        print('"{}" with the score of: {}'.format(high_score_player, high_score).center(150))
        print(border.center(150))
        print('\n')
        input('\nPress [Enter] to continue...')        
              
    
#Automatic Initiation

if __name__ == '__main__':
    START_GAME() 

    

