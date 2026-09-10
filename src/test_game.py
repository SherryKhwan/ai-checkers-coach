from game import Game
from piece import Piece
from move import Move

game = Game()

# Clear the board
game.board.board = [[None for _ in range(8)] for _ in range(8)]

# Set up a multiple capture
game.board.board[2][1] = Piece("black")
game.board.board[3][2] = Piece("white")
game.board.board[5][4] = Piece("white")

print("Current player:", game.current_player)

# First capture
move1 = Move(2, 1, 4, 3, captured=(3, 2))
next_captures = game.make_move(move1)

print("After first capture:")
print("Current player:", game.current_player)
print("Forced piece:", game.forced_piece)
print("Next captures:", next_captures)

# Second capture
move2 = Move(4, 3, 6, 5, captured=(5, 4))
game.make_move(move2)

print("After second capture:")
print("Current player:", game.current_player)
print("Forced piece:", game.forced_piece)