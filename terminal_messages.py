from utils import clean, O
from board import is_game_draw, did_player_win, is_position_available

def initial_message():
  '''
    Display the game initial message.
  '''

  clean()
  with open('./messages/initial_message.txt', encoding='utf8') as f:
    for line in f:
      print(line.strip())
  input()

def get_player_choice_if_it_want_to_go_first():
  '''
    Get the player choice if it want to go first or no.

      Returns:
        choice (str): The choice Y or N
  '''

  clean()
  
  choice = ''

  while choice != 'Y' and choice != 'N':
    try:
      choice = input('Want to be the first to start?[y/n]: ').upper()
    except (EOFError, KeyboardInterrupt):
      print('Bye')
      exit()
    except (KeyError, ValueError):
      print('Not a valid key')
  
  return choice

def game_over_message(board):
  '''
    Print the game over message based on the board disposition.

      Parameters:
        board (list): The board
  '''

  clean()
  if(is_game_draw(board)):
    file_name = 'draw.txt'
  elif did_player_win(board, O):
    file_name = 'win.txt'
  else:
    file_name = 'lose.txt'

  with open('./messages/' + file_name, encoding='utf8') as f:
    for line in f:
      print(line.strip())