from src.game import Game

positions_evaluated = 0

def evaluate_board(board):
    score = 0

    for row_index, row in enumerate(board.board):
        for piece in row:
            if piece is None:
                continue

            value = 3 if piece.is_king else 1

            if not piece.is_king:
                if piece.color == "black":
                    value += row_index * 0.1
                else:
                    value += (7 - row_index) * 0.1

            if piece.color == "black":
                score += value
            else:
                score -= value

    return score


def minimax(game, depth, maximizing_player, alpha=float("-inf"), beta=float("inf")):
    global positions_evaluated
    positions_evaluated += 1

    if depth == 0 or game.is_game_over():
        return evaluate_board(game.board)
    
    legal_moves = game.get_legal_moves()
    legal_moves.sort(key=lambda move: move.is_capture, reverse=True)

    if maximizing_player:
        best_score = float("-inf")

        for move in legal_moves:
            copied_game = copy_game(game)
            copied_game.make_move(move)

            next_depth = depth - 1
            if copied_game.current_player == game.current_player:
                next_depth = depth

            score = minimax(
                copied_game,
                next_depth,
                copied_game.current_player == "black",
                alpha,
                beta
            )

            best_score = max(best_score, score)
            alpha = max(alpha, best_score)

            if beta <= alpha:
                break

        return best_score


    else:
        best_score = float("inf")

        for move in legal_moves:
            copied_game = copy_game(game)
            copied_game.make_move(move)

            next_depth = depth - 1
            if copied_game.current_player == game.current_player:
                next_depth = depth

            score = minimax(
                copied_game,
                next_depth,
                copied_game.current_player == "black",
                alpha,
                beta
            )

            best_score = min(best_score, score)
            beta = min(beta, best_score)

            if beta <= alpha:
                break

        return best_score


def copy_game(game):
    copied_game = Game()

    copied_game.board = game.board.copy()
    copied_game.current_player = game.current_player
    copied_game.forced_piece = game.forced_piece

    return copied_game

def choose_best_move(game, depth=3):
    legal_moves = game.get_legal_moves()
    legal_moves.sort(key=lambda move: move.is_capture, reverse=True)

    if not legal_moves:
        return None

    maximizing_player = game.current_player == "black"
    best_move = None

    if maximizing_player:
        best_score = float("-inf")
    else:
        best_score = float("inf")

    alpha = float("-inf")
    beta = float("inf")

    for move in legal_moves:
        copied_game = copy_game(game)
        copied_game.make_move(move)

        next_depth = depth - 1
        if copied_game.current_player == game.current_player:
            next_depth = depth

        score = minimax(
            copied_game,
            next_depth,
            copied_game.current_player == "black",
            alpha,
            beta
        )

        if maximizing_player and score > best_score:
            best_score = score
            best_move = move
        elif not maximizing_player and score < best_score:
            best_score = score
            best_move = move

        if maximizing_player:
            alpha = max(alpha, best_score)
        else:
            beta = min(beta, best_score)

    return best_move