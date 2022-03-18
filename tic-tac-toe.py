from math import inf as infinity
from random import choice
import platform
import time
from os import system

X = 1
O = 2

board = [
  1, 1, 2,
  1, 2, 1,
  2, 2, 1
]

winning_combinations = [
  [0,1,2],
  [3,4,5],
  [6,7,8],
  [0,3,6],
  [1,4,7],
  [2,5,8],
  [0,4,8],
  [2,4,6]
]

def did_player_win(player, board):
  for i in range(len(winning_combinations)):
    if board[winning_combinations[i][0]] == player and board[winning_combinations[i][1]] == player and board[winning_combinations[i][2]] == player:
      return True
  return False

def is_game_over(board):
  if did_player_win(O, board) or did_player_win(X, board) or not (0 in board):
    return True
  return False

def empty_cells(state):
  cells = []

  for x, row in enumerate(state):
    for y, cell in enumerate(row):
      if cell == 0:
        cells.append([x, y])

  return cells

def is_position_available(board, x, y):
  return board[x][y] == 0

def set_move(x, y, player):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False

def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render(board):
  chars = {
    1: 'X',
    2: 'O',
    0: ' '
  }
  str_line = '---------------'

  print('\n' + str_line)
  for position in range(9):
    symbol = chars[board[position]]
    print(f'| {symbol} |', end='')
    if((position + 1) % 3 == 0):
      print('\n' + str_line)


# print(did_player_win(O, board))
# print(did_player_win(X, board))
# print(is_game_over(board))

clean()
render(board)