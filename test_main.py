import pytest

from main import move, get_white_tile, UP, DOWN, RIGHT, LEFT, h1, h2, h3, BOARD_SIZE, copy_board


def test_get_white_tile():
    board = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]]
    assert get_white_tile(board) == (0, 0)


def test_get_white_tile_2():
    board = [[1, 2, 5],
             [3, 4, 8],
             [6, 7, 0]]
    assert get_white_tile(board) == (2, 2)


def test_get_white_tile_no_zero():
    board = [[1, 1, 2],
             [3, 4, 5],
             [6, 7, 8]]
    with pytest.raises(Exception) as e_info:
        move(board, UP)
    assert str(e_info.value) == 'Array does not contains 0.'


def test_move_up():
    board = [[3, 1, 2],
             [0, 4, 5],
             [6, 7, 8]]
    expected_board = [[0, 1, 2],
                      [3, 4, 5],
                      [6, 7, 8]]
    move(board, UP)
    assert board == expected_board


def test_move_up_borders():
    board = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]]
    with pytest.raises(Exception) as e_info:
        move(board, UP)
    assert str(e_info.value) == 'Tile 0 could not been moved.'


def test_move_down():
    board = [[3, 1, 2],
             [0, 4, 5],
             [6, 7, 8]]
    expected_board = [[3, 1, 2],
                      [6, 4, 5],
                      [0, 7, 8]]
    move(board, DOWN)
    assert board == expected_board


def test_move_down_borders():
    board = [[3, 1, 2],
             [6, 4, 5],
             [0, 7, 8]]
    with pytest.raises(Exception) as e_info:
        move(board, DOWN)
    assert str(e_info.value) == 'Tile 0 could not been moved.'


def test_move_right():
    board = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]]
    expected_board = [[1, 0, 2],
                      [3, 4, 5],
                      [6, 7, 8]]
    move(board, RIGHT)
    assert board == expected_board


def test_move_right_borders():
    board = [[1, 2, 0],
             [3, 4, 5],
             [6, 7, 8]]
    with pytest.raises(Exception) as e_info:
        move(board, RIGHT)
    assert str(e_info.value) == 'Tile 0 could not been moved.'


def test_move_left():
    board = [[1, 2, 0],
             [3, 4, 5],
             [6, 7, 8]]
    expected_board = [[1, 0, 2],
                      [3, 4, 5],
                      [6, 7, 8]]
    move(board, LEFT)
    assert board == expected_board


def test_move_left_borders():
    board = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]]
    with pytest.raises(Exception) as e_info:
        move(board, LEFT)
    assert str(e_info.value) == 'Tile 0 could not been moved.'


def test_h1_some_misplaced_tiles():
    board = [[3, 1, 2],
             [6, 4, 5],
             [7, 0, 8]]
    assert h1(board) == 4


def test_h1_no_misplaced_tiles():
    board = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]]
    assert h1(board) == 0


def test_h1_all_misplaced_tiles():
    board = [[3, 4, 1],
             [6, 0, 2],
             [7, 8, 5]]
    assert h1(board) == 9


def test_h2_no_misplaced_tiles():
    board = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]]
    assert h2(board) == 0


def test_h2_misplaced_tiles():
    board = [[3, 1, 2],
             [6, 4, 5],
             [7, 0, 8]]
    assert h2(board) == 6


def test_h3_no_misplaced_tiles():
    board = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]]
    assert h3(board) == BOARD_SIZE


def test_h3_misplaced_tiles():
    board = [[3, 1, 2],
             [6, 4, 5],
             [7, 0, 8]]
    assert h3(board) == 45  # 6 + 3 * 13


def test_copy_board():
    board = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]]
    board_copy = copy_board(board)
    assert board_copy is not board
    assert board_copy == board
