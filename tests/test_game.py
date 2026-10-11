from src.game import Game
from src.piece import Piece
from src.move import Move

def test_black_moves_first():
    game = Game()

    assert game.current_player == "black"


def test_turn_switches_after_normal_move():
    game = Game()

    move = game.get_legal_moves()[0]
    game.make_move(move)

    assert game.current_player == "white"


def test_capture_is_mandatory():
    game = Game()

    # Create a simple custom board
    game.board.board = [[None for _ in range(8)] for _ in range(8)]

    # Black piece can capture the white piece
    game.board.board[2][1] = Piece("black")
    game.board.board[3][2] = Piece("white")

    # Give black another piece with an ordinary move available
    game.board.board[2][5] = Piece("black")

    legal_moves = game.get_legal_moves()

    # Every legal move must be a capture
    assert len(legal_moves) == 1
    assert legal_moves[0].is_capture
    assert legal_moves[0] == Move(2, 1, 4, 3, captured=(3, 2))


def test_multiple_capture_keeps_same_turn():
    game = Game()

    game.board.board = [[None for _ in range(8)] for _ in range(8)]
    game.board.board[2][1] = Piece("black")
    game.board.board[3][2] = Piece("white")
    game.board.board[5][4] = Piece("white")

    first_capture = game.get_legal_moves()[0]
    game.make_move(first_capture)

    assert game.current_player == "black"
    assert game.forced_piece == (4, 3)
    assert len(game.get_legal_moves()) == 1


def test_game_over_when_current_player_has_no_moves():
    game = Game()

    game.board.board = [[None for _ in range(8)] for _ in range(8)]
    game.board.board[7][0] = Piece("white")

    assert game.is_game_over() is True
    assert game.get_winner() == "white"
