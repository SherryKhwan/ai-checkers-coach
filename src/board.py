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
        for row in self.board:
            print(" ".join(str(piece) for piece in row))


if __name__ == "__main__":
    board = Board()
    board.display()