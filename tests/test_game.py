from src.game import Game


def test_black_moves_first():
    game = Game()

    assert game.current_player == "black"
