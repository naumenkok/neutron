from neutron import Piece, Color, Board, Empty


def test_input_coordinates_to_xy(monkeypatch):
    board = Board()
    monkeypatch.setattr('builtins.input', lambda _: "1 1")
    result = board.enter_and_check(0, 0)
    assert result == (0, 0)

def test_enter_coordinates(monkeypatch):
    board = Board()
    monkeypatch.setattr('builtins.input', lambda _: "End game")
    result = board.enter_coordinates(0)
    assert result == (0, 0)
