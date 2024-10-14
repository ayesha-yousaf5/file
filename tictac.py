def create_board():
  board = [' ' for _ in range(9)]
  return board

def print_board(board):
  for i in range(0, 9, 3):
    print(board[i] + '|' + board[i+1] + '|' + board[i+2])
    if i < 6:
      print('-' * 9)

def check_win(board, player):
  win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
  for combo in win_combinations:
    if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
      return True
  return False

def check_tie(board):
  return ' ' not in board

def play_game():
  board = create_board()
  current_player = 'X'
  while True:
    print_board(board)
    move = int(input(f"Player {current_player}, enter your move (1-9): "))
    if board[move - 1] == ' ':
      board[move - 1] = current_player
      if check_win(board, current_player):
        print_board(board)
        print(f"Player {current_player} wins!")
        break
      if check_tie(board):
        print_board(board)
        print("It's a tie!")
        break
      current_player = 'O' if current_player == 'X' else 'X'
    else:
      print("Invalid move. Please try again.")

play_game()
