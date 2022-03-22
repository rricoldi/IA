from math import inf as infinity
from random import choice, randint
import platform
import time
from os import system

X = 1
O = 2

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

def evaluate(board):
  if did_player_win(board, X):
    score = +1
  elif did_player_win(board, O):
    score = -1
  else:
    score = 0

  return score

def did_player_win(board, symbol):
  for i in range(len(winning_combinations)):
    if board[winning_combinations[i][0]] == symbol and board[winning_combinations[i][1]] == symbol and board[winning_combinations[i][2]] == symbol:
      return True
  return False

def is_game_over(board):
  if did_player_win(board, O) or did_player_win(board, X) or is_game_draw(board):
    return True
  return False

def is_game_draw(board):
  if not (0 in board):
    return True
  return False

def empty_cells(board):
  cells = []

  for x in range(len(board)):
    if(board[x] == 0):
      cells.append(x)

  return cells

def is_position_available(board, position):
  return board[position] == 0


def set_move(board, position, symbol):
  if is_position_available(board, position):
    board[position] = symbol
    return True
  else:
    return False

def clean():
  os_name = platform.system().lower()
  if 'windows' in os_name:
    system('cls')
  else:
    system('clear')


def render(board):
  chars = {
    1: 'X',
    2: 'O',
  }
  str_line = '---------------'

  print('\n' + str_line)
  for position in range(9):
    if board[position] != 0:
      symbol = chars[board[position]]
    else:
      symbol = position

    print(f'| {symbol} |', end='')

    if((position + 1) % 3 == 0):
      print('\n' + str_line)


# print(did_player_win(O, board))
# print(did_player_win(X, board))
# print(is_game_over(board))

def initial_message():
  clean()
  print('Welcome to Tic Tac Toe!')
  print('You will play with an A.I. with the symbol O.')
  print('You can never win.')
  print('Press any key to play ...')
  input()

def choose_if_player_goes_first():
  clean()
  
  first = ''

  while first != 'Y' and first != 'N':
    try:
      first = input('Want to be the first to start?[y/n]: ').upper()
    except (EOFError, KeyboardInterrupt):
      print('Bye')
      exit()
    except (KeyError, ValueError):
      print('Not a valid key')
  
  return first

def minimax(board, depth, symbol):
  opposite_symbol = X
  best = [-1, +infinity]

  if symbol == X:
    opposite_symbol = O
    best = [-1, -infinity]

  if depth == 0 or is_game_over(board):
    score = evaluate(board)
    return [-1, score]

  available_cells = empty_cells(board)

  for position in available_cells:
    board[position] = symbol
    score = minimax(board, depth - 1, opposite_symbol)
    board[position] = 0
    score[0] = position

    if symbol == X:
      if score[1] > best[1]:
        best = score  # max value
    else:
      if score[1] < best[1]:
        best = score  # min value

  return best

def ai_turn(board):
  depth = len(empty_cells(board))
  if depth == 0 or is_game_over(board):
    return

  if depth == 9:
    position = choice([0, 2, 6, 8])
  else:
    position = minimax(board, depth, X)[0]

  set_move(board, position, X)

def human_turn(board):
  position = int(input('Choose a position (number on board): '))

  while position > 8 or position < 0 or not is_position_available(board, position):
    print('Position not available')
    position = int(input('Choose a position (number on board): '))

  set_move(board, position, O)

def main():
  board = [
    0, 0, 0,
    0, 0, 0,
    0, 0, 0
  ]

  initial_message()

  first = choose_if_player_goes_first()

  if first == 'N':
    ai_turn(board)
    first = ''
  
  while not is_game_over(board):
    clean()
    render(board)
    print('\n')

    human_turn(board)

    clean()
    render(board)
    
    if is_game_over(board):
      break

    ai_turn(board)

  clean()
  render(board)

  if(is_game_draw(board)):
    print('Draw!')
  elif did_player_win(board, O):
    print('You won!')
  else:
    print('You lost!')

  exit()

if __name__ == '__main__':
  main()