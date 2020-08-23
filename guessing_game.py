import random
import os

border = ('═' * 50)
border2 = ('█' * 50)
press_enter = 'Press [Enter] to continue...'
game_info = '''
    A random number from 1-10 has been randomly selected.
    For every guess, your score points will add up.
    Try to guess the random number with the least amount 
    of guesses in order to claim 1st place!
'''


def INVALID_OPTION():
    print('Please enter a valid entery.\n')
    input(press_enter)

def CLEAR():
    os.system('clear' if os.name == 'posix' else 'cls')

def START_GAME():
    game_running = True
    high_score = None 
    high_score_player = "Charlie"
    while game_running:
        title_looping = True
        while title_looping:
            try:    # Main Menu
                CLEAR()
                print(border + '\n\tNumber Guessing Game!\n' + '\tby Carlos A. Marin\n' + border + '\n\n')
                print(border2 + '\n█ 1. Play Game  █ 2. #1 player!  █ 3. Quit Game  █\n' + border2)
                selection = int(input('\n\nEnter one of the corresponding numbers: '))
            except ValueError:
                CLEAR()
                INVALID_OPTION()
                continue
            else:
                if selection == 1:    # Play/Replay
                    replay, high_score, high_score_player = game_instance(high_score, high_score_player) 
                    if replay:
                        continue 
                    else:  
                        game_running = False
                        champion(high_score, high_score_player)
                        break
                elif selection == 2:    # High Score Board
                    menu_high_score(high_score, high_score_player)
                elif selection == 3:    # Quit
                    asking_to_quit = True
                    while asking_to_quit:
                        CLEAR()
                        quitting = menu_end_game()
                        if quitting: 
                            champion(high_score, high_score_player)
                            game_running, title_looping = False, False
                        else:
                            pass
                        break
                elif selection not in range(1,4):   # invalid selection.
                    CLEAR()
                    INVALID_OPTION()
                    CLEAR()

def game_instance(high_score, high_score_player):
    answer = random.randint(1, 11)
    score = 0
    CLEAR()
    print('\n\n' + border)
    player = input('Enter player name: ')
    CLEAR()
    if high_score == None:
        print('\nWelcome, {}!\n'.format(player) +  border + game_info)
        print('There are no previous plays therefore no high score has been set.\nEnjoy!\n')
        input(press_enter)
    else:
        print('\nWelcome, {}!\n'.format(player) +  border + game_info)
        print('1st place is currently held by {}, with the score of "{}"\nEnjoy!\n'.format(high_score_player, high_score))
        input(press_enter)
    CLEAR()
    game_looping = True
    while game_looping:
        try:
            if high_score == None:
                print(border + '\n\tPlayer: {}  |  Score: {}'.format(player, score) + '\n' + border)
                print('\n\n' + border2 + '\n█' + 'High Score: None'.center(48) + '█\n' + border2 + '\n')
                guess = int(input('Guess a number between 1-10: '))
            else:
                print(border + '\n\tPlayer: {}  |  Score: {}\n'.format(player, score) + border + '\n')
                champion = ('█' + 'The current high score: "{}" by player: "{}"'.format(high_score, high_score_player).center(48) + '█')
                print('█' * len(champion)) # special border - auto adjust size
                print(champion)
                print('█' * len(champion)) # special border - auto adjust size
                print('\n')
                guess = int(input('Guess a number between 1-10: '))
            score += 1
            CLEAR()
            if guess not in range(1, 11):
                CLEAR()
                print('\nYou must guess in the range of 1-10.\n')
                input(press_enter)
                CLEAR()
            elif guess > answer:
                CLEAR()
                print('\nYour guess of "{}" is greater than the random number.\n'.format(guess))
                input(press_enter)
                CLEAR()
            elif guess < answer:
                CLEAR()
                print('\nYour guess of "{}" is less than the random number.\n'.format(guess))
                input(press_enter)
                CLEAR()
            elif guess == answer:
                high_score, high_score_player = check_high_score(score, high_score, player, high_score_player) # determine if current game surpasses previous scores
                playing_boolean = final_end_game() # determine if player wishes to continue
                return playing_boolean, high_score, high_score_player   # every game instance returns [boolean, integer, string]
        except ValueError:
            CLEAR()
            INVALID_OPTION()
            CLEAR()
    
        
#=========================================================================================================================================

    # Menu option 2
def menu_high_score(high_score, high_score_player): 
    CLEAR()
    if high_score == None:
        print(border + '\n\nThere are no scores posted...\n\n' + border)
        input(press_enter)
    else:
        print(border + '\n\n{} is the champion with the score of "{}"\n\n'.format(high_score_player, high_score) + border + '\n')
        input(press_enter)
        CLEAR()

    # Menu option 3
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
            
            

    # determines high_score and, high_score_player.
def check_high_score(score, high_score, player, high_score_player): 
    CLEAR()
    print('\nYou\'ve guessed the correct number!\nYour score is "{}"\n\n\n'.format(score) + border)
    if high_score == None:
        high_score = score 
        high_score_player = player
        print('The new high score is: "{}" by the player "{}"\n'.format(high_score, high_score_player))
        input(press_enter)
    elif score <= high_score:
        CLEAR()
        print('Congratulations, {}! You hold 1st place!\n'.format(player))
        print('The previous high score is: "{}" by the player "{}"\n'.format(high_score, high_score_player) + border)
        print('\n Your score is: "{}"'.format(score).center(50))
        input(press_enter)
        high_score = score
        high_score_player = player
    else:
        print('Sorry, but your score of "{}" does not surpass the score of "{}" by the player "{}"\n\n'.format(score, high_score, high_score_player) + border)
        input(press_enter)
    return high_score, high_score_player

    # Asking for a replay
def final_end_game():
        loopy = True
        while loopy:
            CLEAR()
            print('Would you like to replay?')
            final_break = input('All data will be lost once game session is ended. ([Y]es/[N]o): ').upper()
            if final_break == 'Y' or final_break == 'YES':
                return True
            elif final_break == 'N' or final_break == 'NO':
                return False
            else:
                CLEAR()
                INVALID_OPTION()
                continue
                
    # Shows winner at the end of the game.         
def champion(high_score, high_score_player):
    CLEAR()
    if high_score == None:
        pass
    else:
        print(border.center(50))
        print('The Champion is....\n'.center(50))
        print('"{}" with the score of: {}'.format(high_score_player, high_score).center(50))
        print(border.center(50))
        print('\n')
        input(press_enter)        
              
    
# Automatic Initiation

if __name__ == '__main__':
    START_GAME() 

    

