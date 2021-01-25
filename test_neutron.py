from neutron import Piece, Color, Board, Empty


# def test_input_coordinates_to_xy(monkeypatch):
#     board = Board()
#     monkeypatch.setattr('builtins.input', lambda _: "1 1")
#     result = board.enter_and_check(0, 0)
#     assert result == (0, 0)

# def test_enter_coordinates(monkeypatch):
#     board = Board()
#     monkeypatch.setattr('builtins.input', lambda _: "End game")
#     result = board.enter_coordinates(0)
#     assert result == (0, 0)

# def test_variant_rec():
#     board = Board()
#     result = board.variant_rec(3, 1)
#     assert result == []


def test_probability_of_winning():
    board = Board()
    result = board.probability_of_winning(3, 1)
    assert result == {(1, 3): 0.2, (4, 2): 0.2, (1, 1): 0.5, (3, 3): 0.33, (4, 1): 0.33}


def test_choose_coordinates_for_clever():
    board = Board()
    result = board.choose_coordinates_for_clever(1, 3)
    assert result == (1, 3)
