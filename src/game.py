from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = "black"
        self.forced_piece = None  # Track the piece that must continue capturing

    def switch_player(self):
        self.current_player = "white" if self.current_player == "black" else "black"

    def get_legal_moves(self):
        if self.forced_piece is not None:
            row, col = self.forced_piece
            return self.board.get_piece_captures(row, col)

        return self.board.get_all_moves(self.current_player)            

    def make_move(self, move):
        """Attempt to make a move for the current player.

        Raises ValueError if the move is not legal.
        """
        legal = self.get_legal_moves()

        if move not in legal:
            raise ValueError(f"Illegal move: {move}")

        next_captures = self.board.make_move(move)

        if next_captures:
            self.forced_piece = move.to_square
            return next_captures
        else:
            self.forced_piece = None
            self.switch_player()
            return []