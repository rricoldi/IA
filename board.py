from utils import X, O

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

def human_turn(board):
  '''
    move the player to its desired position, if it is available.

      Parameters:
        board (list): The board
  '''

  position = int(input('Choose a position (number on board): '))

  while position > 8 or position < 0 or not is_position_available(board, position):
    print('Position not available')
    position = int(input('Choose a position (number on board): '))
  set_move(board, position, O)

def did_player_win(board, symbol):
  '''
    Verify if the symbol won the game.

      Parameters:
        board (list): The board
        symbol (int): X literal[1] if A.I. and O literal [2] if human

      Returns:
        result (boolean): True if player won, False otherwise
  '''

  for i in range(len(winning_combinations)):
    if board[winning_combinations[i][0]] == symbol and board[winning_combinations[i][1]] == symbol and board[winning_combinations[i][2]] == symbol:
      return True
  return False

def is_game_over(board):
  '''
    Verify if the game is over.

      Parameters:
        board (list): The board

      Returns:
        result (boolean): True if game is over, False otherwise
  '''

  if did_player_win(board, O) or did_player_win(board, X) or is_game_draw(board):
    return True
  return False

def is_game_draw(board):
  '''
    Verify if the game is draw.

      Parameters:
        board (list): The board

      Returns:
        result (boolean): True if game is draw, False otherwise
  '''

  if not (0 in board):
    return True
  return False

def empty_positions(board):
  '''
    Return board's empty positions.

      Parameters:
        board (list): The board

      Returns:
        positions (list): positions available to move
  '''

  cells = []

  for x in range(len(board)):
    if(board[x] == 0):
      cells.append(x)

  return cells

def is_position_available(board, position):
  '''
    Verify if position is available on the board.

      Parameters:
        board (list): The board
        position (int): position to be verified

      Returns:
        result (boolean): True if position is available, False otherwise
  '''

  return board[position] == 0


def set_move(board, position, symbol):
  '''
    Try to set the symbol on the board's position.

      Parameters:
        board (list): The board
        position (int): position to be moved
        symbol (int): X literal[1] if A.I. and O literal [2] if human

      Returns:
        result (boolean): True if move was permitted, False otherwise
  '''

  if is_position_available(board, position):
    board[position] = symbol
    return True
  else:
    return False