from piece import Piece


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


if __name__ == "__main__":
    board = Board()
    board.display()