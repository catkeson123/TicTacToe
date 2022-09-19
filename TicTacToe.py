#!/usr/bin/env python
# coding: utf-8

# In[2]:


from IPython.display import clear_output


# In[3]:


def display_board(board):
    clear_output()
    print('Current game board:')
    print(' ' + board[1] + '|' + board[2] + '|' + board[3])
    print('-------')
    print(' ' + board[4] + '|' + board[5] + '|' + board[6])
    print('-------')
    print(' ' + board[7] + '|' + board[8] + '|' + board[9])


# In[4]:


def player_choice():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# In[5]:


def place_marker(board, position, marker):
    board[position] = marker


# In[6]:


from random import randint

# assigns who goes first
def goes_first():  
    if randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'


# In[7]:


def space_check(board, position):
    return board[position] == ' '


# In[8]:


def win_check(board,marker):
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or
            (board[4] == marker and board[5] == marker and board[6] == marker) or
            (board[7] == marker and board[8] == marker and board[9] == marker) or
            (board[1] == marker and board[4] == marker and board[7] == marker) or
            (board[2] == marker and board[5] == marker and board[8] == marker) or
            (board[3] == marker and board[6] == marker and board[9] == marker) or
            (board[1] == marker and board[5] == marker and board[9] == marker) or
            (board[3] == marker and board[5] == marker and board[7] == marker))


# In[9]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[10]:


def player_position(board):
    position = '0'
    accept_range = [1,2,3,4,5,6,7,8,9]
    
    while position not in accept_range or not space_check(board,position):
        position = int(input('Choose next position (1-9): '))
        
    return position


# In[11]:


def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# In[12]:


def ready_to_play():
    ready = ''
    
    while ready != 'y' and ready != 'n':
        ready = input('Are you ready to play? Enter y or n:')
            
    return ready


# In[ ]:


print ('Welcome to Tic Tac Toe!')

while True:
    # sets the board
    board = [' ']*10
    player1_marker, player2_marker = player_choice()
    turn = goes_first()
    print(turn + ' will go first!')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        display_board(board)
  
        if turn == 'Player 1':
            display_board(board)
            position = player_position(board)
            place_marker(board, position, player1_marker)
            
            if win_check(board, player1_marker):
                display_board(board)
                print('Player 1 has won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Its a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(board)
            position = player_position(board)
            place_marker(board, position, player2_marker)
            
            if win_check(board, player2_marker):
                display_board(board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Its a draw!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break

