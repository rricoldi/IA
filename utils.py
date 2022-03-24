import platform
from os import system

X = 1
O = 2

def clean():
  '''
    Clean the terminal.
  '''

  os_name = platform.system().lower()
  if 'windows' in os_name:
    system('cls')
  else:
    system('clear')


def render(board):
  '''
    Print the board on the terminal.

      Parameters:
        board (list): The board
  '''

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

def clean_and_render_board(board):
  '''
    Clean the terminal and print the board on it.

      Parameters:
        board (list): The board
  '''

  clean()
  render(board)

