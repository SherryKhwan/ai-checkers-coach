
from src.board import Board
from src.piece import Piece
from src.game import Game
from src.ai import evaluate_board, minimax, choose_best_move


def test_evaluate_board_counts_pieces():
    board = Board()
    board.board = [[None for _ in range(8)] for _ in range(8)]

    board.board[2][1] = Piece("black")
    board.board[3][2] = Piece("black")
    board.board[4][3] = Piece("white")

    assert evaluate_board(board) == 1.2


def test_king_is_worth_three_points():
    board = Board()
    board.board = [[None for _ in range(8)] for _ in range(8)]

    board.board[2][1] = Piece("black", is_king=True)

    assert evaluate_board(board) == 3


def test_board_copy_is_independent():
    board = Board()
    board.board = [[None for _ in range(8)] for _ in range(8)]
    board.board[2][1] = Piece("black")

    copied_board = board.copy()

    copied_board.board[2][1].is_king = True

    assert board.board[2][1].is_king is False
    assert copied_board.board[2][1].is_king is True


def test_minimax_finds_benefit_of_capture():
    game = Game()

    # Clear the board.
    game.board.board = [
        [None for _ in range(8)]
        for _ in range(8)
    ]

    # Place a black piece and a white piece that black can capture.
    game.board.board[2][1] = Piece("black")
    game.board.board[3][2] = Piece("white")

    score = minimax(game, depth=1, maximizing_player=True)

    assert score == 1.4


def test_choose_best_move_returns_legal_move():
    game = Game()

    move = choose_best_move(game, depth=1)

    assert move in game.get_legal_moves()


def test_ai_must_choose_capture_when_available():
    game = Game()

    # Clear the board.
    game.board.board = [
        [None for _ in range(8)]
        for _ in range(8)
    ]

    # Black can capture the white piece at (3, 2).
    game.board.board[2][1] = Piece("black")
    game.board.board[3][2] = Piece("white")

    # Add another black piece with an ordinary move available.
    game.board.board[2][5] = Piece("black")

    move = choose_best_move(game, depth=1)

    assert move is not None
    assert move.is_capture


def test_ai_prefers_capture_that_wins_a_piece():
    game = Game()

    game.board.board = [
        [None for _ in range(8)]
        for _ in range(8)
    ]

    game.board.board[2][1] = Piece("black")
    game.board.board[3][2] = Piece("white")
    game.board.board[5][6] = Piece("white")

    move = choose_best_move(game, depth=1)

    assert move is not None
    assert move.is_capture
    assert move.from_square == (2, 1)


def test_advanced_piece_has_higher_score():
    game = Game()

    # Clear the board.
    game.board.board = [
        [None for _ in range(8)]
        for _ in range(8)
    ]

    # Black piece farther from promotion.
    game.board.board[1][2] = Piece("black")
    early_score = evaluate_board(game.board)

    # Move the same piece closer to promotion.
    game.board.board[1][2] = None
    game.board.board[5][2] = Piece("black")
    advanced_score = evaluate_board(game.board)

    assert advanced_score > early_score


def test_white_piece_advancement_increases_its_value():
    board = Board()
    board.board = [[None for _ in range(8)] for _ in range(8)]

    board.board[6][1] = Piece("white")
    early_score = evaluate_board(board)

    board.board[6][1] = None
    board.board[2][1] = Piece("white")
    advanced_score = evaluate_board(board)

    assert advanced_score < early_score


def test_ai_can_search_multiple_moves_ahead():
    game = Game()

    move = choose_best_move(game, depth=3)

    assert move is not None
    assert move in game.get_legal_moves()


def test_minimax_accounts_for_opponents_response():
    game = Game()

    game.board.board = [
        [None for _ in range(8)]
        for _ in range(8)
    ]

    # Black has a piece that white may be able to capture.
    game.board.board[2][1] = Piece("black")
    game.board.board[5][4] = Piece("black")
    game.board.board[3][2] = Piece("white")

    move = choose_best_move(game, depth=3)

    assert move is not None
    assert move in game.get_legal_moves()


def test_ai_returns_legal_move_at_depth_four():
    game = Game()

    move = choose_best_move(game, depth=4)

    assert move is not None
    assert move in game.get_legal_moves()