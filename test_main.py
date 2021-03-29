import pytest

from main import move, get_white_tile, UP, DOWN, RIGHT, LEFT, copy_board


def test_get_white_tile():
    t = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]
    assert get_white_tile(t) == (0, 0)


def test_get_white_tile_2():
    t = [[1, 2, 5],
         [3, 4, 8],
         [6, 7, 0]]
    assert get_white_tile(t) == (2, 2)


def test_get_white_tile_no_zero():
    t = [[1, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]
    with pytest.raises(Exception) as e_info:
        move(UP, t)
    assert str(e_info.value) == 'Array does not contains 0.'


def test_move_up():
    t = [[3, 1, 2],
         [0, 4, 5],
         [6, 7, 8]]
    expected_t = [[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]]
    move(UP, t)
    assert t == expected_t


def test_move_up_borders():
    t = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]
    expected_t = [[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]]
    move(UP, t)
    assert t == expected_t


def test_move_down():
    t = [[3, 1, 2],
         [0, 4, 5],
         [6, 7, 8]]
    expected_t = [[3, 1, 2],
                  [6, 4, 5],
                  [0, 7, 8]]
    move(DOWN, t)
    assert t == expected_t


def test_move_down_borders():
    t = [[3, 1, 2],
         [6, 4, 5],
         [0, 7, 8]]
    expected_t = [[3, 1, 2],
                  [6, 4, 5],
                  [0, 7, 8]]
    move(DOWN, t)
    assert t == expected_t


def test_move_right():
    t = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]
    expected_t = [[1, 0, 2],
                  [3, 4, 5],
                  [6, 7, 8]]
    move(RIGHT, t)
    assert t == expected_t


def test_move_right_borders():
    t = [[1, 2, 0],
         [3, 4, 5],
         [6, 7, 8]]
    expected_t = [[1, 2, 0],
                  [3, 4, 5],
                  [6, 7, 8]]
    move(RIGHT, t)
    assert t == expected_t


def test_move_left():
    t = [[1, 2, 0],
         [3, 4, 5],
         [6, 7, 8]]
    expected_t = [[1, 0, 2],
                  [3, 4, 5],
                  [6, 7, 8]]
    move(LEFT, t)
    assert t == expected_t


def test_move_left_borders():
    t = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]
    expected_t = [[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]]
    move(LEFT, t)
    assert t == expected_t


def test_copy_board():
    t = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]
    expected_t = [[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]]
    assert t is not expected_t
    assert t == expected_t
