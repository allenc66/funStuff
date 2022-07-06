from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+ '|' + board[8]+ '|' + board[9])
    print('-|-|-')
    print(board[4]+ '|' + board[5]+ '|' + board[6])
    print('-|-|-')
    print(board[1]+ '|' + board[2]+ '|' + board[3])

def player_input():

    '''
    Output = (Player1_marker, Player2_marker)
    '''
    marker = 'wrong'
    # keep asking player 1 to choose X or O
    while marker != 'X' and marker != 'O':
        marker = input('Player1, choose X or O: ').upper()
    # assign player 2, the opposite marker
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
        print('Player 1 is X and Player 2 is O')
    else:
        player2 = 'X'
        print('Player 1 is O and Player 2 is X')

    return (player1, player2)  


def place_marker(board, marker, position): #no need to verify the X and O, since above player_input has secured X or O.
    board[position] = marker
    

def win_check(board, mark):
   
       return ((board[1] == mark and board[2] == mark and board[3] == mark) or 
       (board[4] == mark and board[5] == mark and board[6] == mark) or 
       (board[7] == mark and board[8] == mark and board[9] == mark) or 
       (board[1] == mark and board[4] == mark and board[7] == mark) or 
       (board[2] == mark and board[5] == mark and board[8] == mark) or 
       (board[3] == mark and board[6] == mark and board[9] == mark) or 
       (board[1] == mark and board[5] == mark and board[9] == mark) or 
       (board[3] == mark and board[5] == mark and board[7] == mark))
         

import random

def choose_first():
    first = random.randint(1,2)
    if first == 1:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Please choose a position: (1-9) '))
    return position

def replay():
    answer = input('Do you want to play again? (Y/N) ').upper()
    return answer == 'Y'


#############################################################################################
print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here

    board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to play? Y or N ').upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        #Player1's turn
            if turn == 'Player 1':
                #show the board
                display_board(board)
                #choose a postion
                position = player_choice(board)
                #place the marker on the position
                place_marker(board, player1_marker,position)
                #check if they won OR chekc if there is a tie
                if win_check(board,player1_marker):
                    display_board(board)
                    print('Player 1 Wins!')
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('Game tied!')
                        break
                    else:
                        turn = 'Player 2'
                #no tie and no win, then next player's turn
                
                
        #Player2's turn
            else:
                 #show the board
                display_board(board)
                #choose a postion
                position = player_choice(board)
                #place the marker on the position
                place_marker(board, player2_marker,position)
                #check if they won OR chekc if there is a tie
                if win_check(board,player2_marker):
                    display_board(board)
                    print('Player 2 Wins!')
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('Game tied!')
                        break
                    else:
                        turn = 'Player 1'

    if not replay():
        break