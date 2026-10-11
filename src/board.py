from src.piece import Piece
from src.move import Move


class Board:
    def __init__(self):
        self.board = self.create_initial_board()

    def create_initial_board(self):
        board = []

        for row in range(8):
            current_row = []

            for col in range(8):
                if row < 3 and (row + col) % 2 == 1:
                    current_row.append(Piece("black"))
                elif row > 4 and (row + col) % 2 == 1:
                    current_row.append(Piece("white"))
                else:
                    current_row.append(None)

            board.append(current_row)

        return board

    def display(self):
        column_labels = "  a b c d e f g h"
        print(column_labels)

        for row_index, row in enumerate(self.board):
            symbols = []

            for piece in row:
                if piece is None:
                    symbols.append(".")
                elif piece.color == "black":
                    symbols.append("b" if piece.is_king else "B")
                elif piece.color == "white":
                    symbols.append("w" if piece.is_king else "W")

            print(f"{8 - row_index} {' '.join(symbols)}")

        print(column_labels)

    def get_piece_moves(self, row, col):
        piece = self.board[row][col]
        if piece is None:
            return []

        moves = []

        if piece.is_king:
            directions = [(1, -1), (1, 1), (-1, -1), (-1, 1)]
        else:
            direction = 1 if piece.color == "black" else -1
            directions = [(direction, -1), (direction, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if self.board[new_row][new_col] is None:
                    moves.append(Move(row, col, new_row, new_col))

        return moves

    def get_piece_captures(self, row, col):
        piece = self.board[row][col]
        if piece is None:
            return []

        captures = []

        if piece.is_king:
            directions = [(1, -1), (1, 1), (-1, -1), (-1, 1)]
        else:
            direction = 1 if piece.color == "black" else -1
            directions = [(direction, -1), (direction, 1)]

        for dr, dc in directions:
            mid_row, mid_col = row + dr, col + dc
            new_row, new_col = row + 2 * dr, col + 2 * dc

            if (
                0 <= mid_row < 8
                and 0 <= mid_col < 8
                and 0 <= new_row < 8
                and 0 <= new_col < 8
            ):
                mid_piece = self.board[mid_row][mid_col]
                if (
                    mid_piece is not None
                    and mid_piece.color != piece.color
                    and self.board[new_row][new_col] is None
                ):
                    captures.append(Move(row, col, new_row, new_col, captured=(mid_row, mid_col)))

        return captures
    
    def get_all_moves(self, color):
        all_moves = []
        all_captures = []

        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece is not None and piece.color == color:
                    captures = self.get_piece_captures(row, col)
                    if captures:
                        all_captures.extend(captures)
                    else:
                        moves = self.get_piece_moves(row, col)
                        all_moves.extend(moves)

        return all_captures if all_captures else all_moves

    def make_move(self, move):
        from_row = move.from_row
        from_col = move.from_col
        to_row = move.to_row
        to_col = move.to_col
        captured = move.captured

        piece = self.board[from_row][from_col]
        if piece is None:
            raise ValueError("There is no piece at the starting position")

        self.board[from_row][from_col] = None

        if captured is not None:
            captured_row, captured_col = captured
            self.board[captured_row][captured_col] = None

        self.board[to_row][to_col] = piece

        if piece.color == "black" and to_row == 7:
            piece.is_king = True
        elif piece.color == "white" and to_row == 0:
            piece.is_king = True

        if captured is not None:
            next_captures = self.get_piece_captures(to_row, to_col)
            return next_captures

        return []

if __name__ == "__main__":
    board = Board()

    board.board = [[None for _ in range(8)] for _ in range(8)]

    board.board[2][1] = Piece("black")
    board.board[3][2] = Piece("white")
    board.board[5][4] = Piece("white")

    move = Move(2, 1, 4, 3, captured=(3, 2))

    board.make_move(move)

    board.display()

    next_captures = board.get_piece_captures(4, 3)

    for move in next_captures:
        print(move, move.captured)