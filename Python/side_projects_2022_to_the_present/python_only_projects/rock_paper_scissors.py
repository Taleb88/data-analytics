#rock, paper, scissors game
import random, sys

wins = 0
losses = 0
draws = 0

while True:
    total_games_played = wins + losses + draws
    print("%s Wins, %s Losses, %s Draws, %s Games Played"%(wins, losses, draws, total_games_played))
    while True:
        print("Make your move: Rock 'r' Paper 'p' Scissors 's' or Quit 'q'")
        user_turn = input().lower()
        if user_turn == 'q':
            print('have a nice day')
            sys.exit() # program is terminated
        if user_turn == 'r' or user_turn == 'p' or user_turn == "s":
            break
        print("Please enter one of the following: 'r', 'p', 's', q.")
    #user input
    if user_turn == 'r':
        print("Rock vs...")
    elif user_turn == 'p':
        print('Paper vs...')
    elif user_turn == 's':
        print('Scissors vs...')
    #user input vs cpu input
    random_num = random.randint(1, 3)
    if random_num == 1:
        cpu_turn = 'r'
        print('Rock')
    elif random_num == 2:
        cpu_turn = 'p'
        print('Paper')
    elif random_num == 3:
        cpu_turn = 's'
        print('Scissors')
    # results
    if user_turn == cpu_turn:
        print('Draw')
        draws += 1
    elif user_turn == 'r' and cpu_turn == 's':
        print('Winner')
        wins += 1
    elif user_turn == 'p' and cpu_turn == 'r':
        print('Winner')
        wins += 1
    elif user_turn == 's' and cpu_turn == 'p':
        print('Winner')
        wins += 1
    elif cpu_turn == 'r' and user_turn == 's':
        print('Loser')
        losses += 1
    elif cpu_turn == 'p' and user_turn == 'r':
        print('Loser')
        losses += 1
    elif cpu_turn == 's' and user_turn == 'p':
        print('Loser')
        losses += 1