import os
from collections import Counter
from collections import defaultdict

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac/Linux
    else:
        os.system('clear')


def display_board(board):
    clear_screen()
    print(board[7]+'|'+board[8]+'|'+ board[9])
    print(board[4]+'|'+board[5]+'|'+ board[6])
    print(board[1]+'|'+board[2]+'|'+ board[3])

test_board = ['#', 'X','O','X','O', 'X', 'O', 'X', 'O', 'X']
display_board(test_board)
display_board(test_board)
display_board(test_board)


def player_input():

    marker = ''
    while marker!= 'X' and marker!= '0':
        marker = input('Player1: Choose X or 0: ').upper()

    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')
    
def place_marker(board, marker, position):
    board[position] = marker

mylist = [1,1,1,1,2,2,2,3,3,4,4,4,4,4]

result = Counter(mylist)

print(result)

sentence = "Count the number of words that appear in this sentence"

print(Counter(sentence.split()))

d = {'Right': 5}

print(d['Right'])

e = defaultdict(lambda : 0)

print(e['wrong key - it will assign it default value. Normal dict would have thrown error'])