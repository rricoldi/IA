from random import choice
from board import set_move, is_game_over, empty_positions
from utils import X
from minimax import minimax

def ai_turn(board):
  '''
    Determine the best move for the A.I., the move is based if it's the first move of the game.
    If it is, chooses one of the corners if it is.
    If it is not, call the minimax algorithm.

      Parameters:
        board (list): The board
  '''
  depth = len(empty_positions(board))
  if depth == 0 or is_game_over(board):
    return

  if depth == 9:
    position = choice([0, 2, 6, 8])
  else:
    position = minimax(board, depth, X)[0]

  set_move(board, position, X)