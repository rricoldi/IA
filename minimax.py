from math import inf as infinity
from board import did_player_win, is_game_over, empty_positions
from utils import X, O

def evaluate(board):
  '''
    Evaluate if the A.I. would win, lose or draw, based on the board disposition.

      Parameters:
        board (list): The board

      Returns:
        score (int): 1 if A.I. wins, -1 if player wins and 0 otherwise
  '''

  if did_player_win(board, X):
    score = +1
  elif did_player_win(board, O):
    score = -1
  else:
    score = 0

  return score

def minimax(board, depth, symbol):
  '''
    Determine the best move for the A.I. using the minimax algorithm.

      Parameters:
        board (list): The board
        depth (int): The number of positions available to move
        symbol (int): X literal[1] if A.I. and O literal [2] if human

      Returns:
        score (int): 1 if A.I. wins, -1 if player wins and 0 otherwise
  '''

  opposite_symbol = X
  best = [-1, +infinity]

  if symbol == X:
    opposite_symbol = O
    best = [-1, -infinity]

  # If the game is over or there are no more empty cells, evaluate the board
  if depth == 0 or is_game_over(board):
    score = evaluate(board)
    return [-1, score]

  available_cells = empty_positions(board)

  # for each position available on the board 
  # we call the minimax function recursively changing the player
  # and choose the move that will be better for the A.I. or worse for the human
  for position in available_cells:
    board[position] = symbol
    current = minimax(board, depth - 1, opposite_symbol)
    board[position] = 0
    current[0] = position

    # if is the A.I. sees if the current score is better then the best
    if symbol == X:
      if current[1] > best[1]:
        best = current
    # if is the human sees if the current score is worse then the best
    else:
      if current[1] < best[1]:
        best = current

  return best