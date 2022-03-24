'''
  Create the board and call the game functions.

  Functions:
    game_loop(list)
    main()
'''

from board import is_game_over, human_turn
from utils import clean_and_render_board
from terminal_messages import get_player_choice_if_it_want_to_go_first, game_over_message, initial_message
from ai import ai_turn

def game_loop(board):
  '''
    Main loop of the game, it switches between A.I. and human turns.

      Parameters:
        board (list): The board
  '''

  while not is_game_over(board):
    clean_and_render_board(board)

    human_turn(board)

    clean_and_render_board(board)
    
    if is_game_over(board):
      break

    ai_turn(board)

def main():
  board = [
    0, 0, 0,
    0, 0, 0,
    0, 0, 0
  ]

  initial_message()

  first = get_player_choice_if_it_want_to_go_first()

  if first == 'N':
    ai_turn(board)
  
  game_loop(board)  

  clean_and_render_board(board)

  game_over_message(board)

  exit()

if __name__ == '__main__':
  main()