from typing import List, Literal


def show_board(board: List[str]) -> None:
  for i in range(0, 9, 3):
    print(f"{board[i]} {board[i+1]} {board[i+2]}     {i} {i+1} {i+2}")


def ask_square(board: List[str]) -> int:
  response = ""
  while not response.isdigit() or not 0 <= int(response) <= 8 or board[int(response)] != ".":
    response = input("Entrez le numéro de la case que vous voulez jouez : ")

  return int(response)


def play_square(current_player: str, board: List[str], square_to_play: int) -> List[str]:
  board[square_to_play] = current_player

  return board


def board_is_full(board: List[str]) -> bool:
  board_is_full = True
  for square in board:
    if square == ".":
      board_is_full = False
      break

  return board_is_full


def winner(board: List[str]):
  winner = None
  if board[0] == board[1] == board[2] == "X" or board[0] == board[1] == board[2] == "O":
    winner = "X" if board[0] == "X" else "O"
  elif board[3] == board[4] == board[5] == "X" or board[3] == board[4] == board[5] == "O":
    winner = "X" if board[3] == "X" else "O"
  elif board[6] == board[7] == board[8] == "X" or board[6] == board[7] == board[8] == "O":
    winner = "X" if board[6] == "X" else "O"
  elif board[0] == board[3] == board[6] == "X" or board[0] == board[3] == board[6] == "O":
    winner = "X" if board[0] == "X" else "O"
  elif board[1] == board[4] == board[7] == "X" or board[1] == board[4] == board[7] == "O":
    winner = "X" if board[1] == "X" else "O"
  elif board[2] == board[5] == board[8] == "X" or board[2] == board[5] == board[8] == "O":
    winner = "X" if board[2] == "X" else "O"
  elif board[0] == board[4] == board[8] == "X" or board[0] == board[4] == board[8] == "O":
    winner = "X" if board[0] == "X" else "O"
  elif board[2] == board[4] == board[6] == "X" or board[2] == board[4] == board[6] == "O":
    winner = "X" if board[2] == "X" else "O"

  return winner


def change_player(current_player: str) -> str:
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"

  return current_player


def main() -> None:
  board = [".", ".", ".", ".", ".", ".", ".", ".", "."]
  current_player = "X"
  while not board_is_full(board=board) and not winner(board=board):
    show_board(board=board)
    print(f"C'est au joueur {current_player} de jouer.")
    square_to_play = ask_square(board=board)
    board = play_square(current_player=current_player, board=board, square_to_play=square_to_play)
    current_player = change_player(current_player=current_player)

  show_board(board=board)

  if winner(board=board):
    print(f"Le gagnant de cette partie est le joueur {winner(board=board)}. Bravo !")
  elif board_is_full(board=board):
    print("Match nul !")



if __name__ == "__main__":
  main()