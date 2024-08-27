import numpy as np
from tabulate import tabulate 

# defining board : 
board = {k+1 : k+1 for k in range(100)}

# ladders : 
board[6] = 24
board[12] = 30
board[22] = 43
board[27] = 35
board[31] = 49
board[47] = 55
board[41] = 58
board[51] = 73
board[64] = 85
board[80] = 82
board[72] = 90
board[86] = 96

# snakes : 
board[98] = 84
board[94] = 88
board[83] = 61
board[87] = 66
board[68] = 49
board[57] = 36
board[48] = 14
board[13] = 7
board[4] = 19

#  ranks 
rank = [] 

# game setup : 
status = {}
print('\n##### WELCOME TO SNAKE & LADDERS #####\n')
num_of_players = int(input("how many players you are? "))
players_name = [input(f"enter player {i+1} : ") for i in range(num_of_players) ]


for p in players_name :
    status[p] = 1

# playing game :

def turn(guy) : 
    
    global status
    print('------------------')
    print(f"{guy} turn!")
    print('------------------\n')
    input("press enter to roll the dice...") 

    dice = np.random.randint(1,7)
    print(f"your dice thrown : {dice}" )
    print('-------------------')

    if (status[guy] + dice) <= 100 :  # updating status only if lesser than or equal to hundred 
        status[guy] += dice
    else :
        print("out of 100...") 

    if board[status[guy]] != status[guy] : # checking for snakes or ladders
        if status[guy] > board[status[guy]] : 
            print("SNAKE :(")
        else : 
            print("LADDER :)")
        status[guy] = board[status[guy]] 
    
    # printing board : 
    table = [[key, value] for key, value in status.items()]
    headers = ["Player", "At"]
    print(tabulate(table, headers, tablefmt="heavy_grid"))
        
    if dice == 6 :
        print("******You've got a second chance********")
        turn(guy)
    
    return check_win(guy) 

def check_win(guy) : 
    return True if status[guy] == 100 else False

def print_winners() : 
    global rank
    table = [[i+1,p] for i,p in enumerate(rank)]
    table.append([num_of_players,(list(set(players_name) - set(rank)))[0]])
    headers = ['Rank' , 'Player']
    print('\nWinners : \n')
    print(tabulate(table, headers, tablefmt="heavy_grid"))
        
while len(rank) != (len(players_name) - 1) :
    for i in range(num_of_players) : 

        if players_name[i] not in rank : 
        
            if turn(players_name[i]) :
        
                rank.append(players_name[i])
                print(f"@@@@@@@@@@@@@@@   {players_name[i].upper()} completed the game at {len(rank)} position  @@@@@@@@@@@@")

                if len(rank) == (len(players_name) - 1) : 
                    break

else : 
    print_winners()


