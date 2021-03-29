import random
from typing import Tuple, List, Union

# Exercise 1

FINAL_STATE = [[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8]]
UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]
BOARD_SIZE = 3


def print_board(board: List[List[int]]):
    for i in range(BOARD_SIZE):
        print(' | '.join(str(s) for s in board[i]))


def move(direction: str, board: List[List[int]]) -> Tuple[int, int]:
    i, j = get_white_tile(board)
    if direction == UP and i - 1 >= 0:
        board[i][j] = board[i - 1][j]
        board[i - 1][j] = 0
        i = i - 1
    elif direction == DOWN and i + 1 < len(board):
        board[i][j] = board[i + 1][j]
        board[i + 1][j] = 0
        i = i + 1
    elif direction == LEFT and j - 1 >= 0:
        board[i][j] = board[i][j - 1]
        board[i][j - 1] = 0
        j = j - 1
    elif direction == RIGHT and j + 1 < len(board[0]):
        board[i][j] = board[i][j + 1]
        board[i][j + 1] = 0
        j = j + 1
    return i, j


def generate_random_configuration(n: int = 100) -> List[List[int]]:
    random_config = copy_board(FINAL_STATE)
    while random_config == FINAL_STATE:
        for k in range(n):
            move(random.choice(DIRECTIONS), random_config)
    return random_config


def copy_board(board: List[List[int]]) -> List[List[int]]:
    new_board = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            new_board[i][j] = board[i][j]
    return new_board


def get_white_tile(board: List[List[int]]) -> Union[Tuple[int, int], None]:
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                return i, j
    raise ValueError('Array does not contains 0.')


# Exercise 2

def breadth_first_search(board: List[List[int]]) -> Tuple[int, int]:
    queue = [board]
    depth = 0
    nodes_visited = 0

    while queue and not queue[0] == FINAL_STATE:
        current_board = queue.pop(0)
        curr_i, curr_y = get_white_tile(current_board)

        for direction in DIRECTIONS:
            board_copy = copy_board(current_board)
            new_i, new_y = move(direction, board_copy)
            if not (new_i == curr_i and new_y == curr_y):
                queue.append(board_copy)
                nodes_visited += 1

        depth += 1

    return depth, nodes_visited


def depth_first_search(board: List[List[int]]) -> Tuple[bool, int, int]:
    stack = []
    seen = []
    stack.append((board, 0))
    nodes_visited = 0
    depth = 0
    while len(stack) != 0:
        nodes_visited += 1
        current_board, depth = stack.pop()
        seen.append(current_board)
        if current_board == FINAL_STATE:
            return True, depth, nodes_visited
        else:
            for direction in DIRECTIONS:
                board_copy = copy_board(current_board)
                move(direction, board_copy)
                if board_copy not in seen:
                    stack.append((board_copy, depth + 1))
    return False, depth, nodes_visited


def depth_first_search_limit(board: List[List[int]], limit: int) -> Tuple[bool, int, int]:
    stack = []
    seen = []
    stack.append((board, 0))
    nodes_visited = 0
    depth = 0
    while len(stack) != 0:
        nodes_visited += 1
        current_board, depth = stack.pop()
        seen.append(current_board)
        if current_board == FINAL_STATE:
            return True, depth, nodes_visited
        else:
            if depth < limit:
                for direction in DIRECTIONS:
                    board_copy = copy_board(current_board)
                    move(direction, board_copy)
                    if board_copy not in seen:
                        stack.append((board_copy, depth + 1))
    return False, depth, nodes_visited


def depth_iterative_search(board: List[List[int]]) -> Tuple[bool, int, int]:
    found = False
    depth = 0
    nodes_visited = 0
    limit = 1
    while not found:
        found, depth, nodes_visited = depth_first_search_limit(board, limit)
        limit += 1
    return found, depth, nodes_visited


# Exercise 3
def h1(board: List[List[int]]) -> int:
    misplaced = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] != FINAL_STATE[i][j]:
                misplaced += 1
    return misplaced


def h2(board: List[List[int]]) -> int:
    total_distance = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            current_tile = board[i][j]
            total_distance += abs(i - int(current_tile / BOARD_SIZE) + abs(j - (current_tile % BOARD_SIZE)))
    return total_distance


def h3(board: List[List[int]]) -> int:
    def _score_sum(b: List[List[int]]) -> int:
        sn = 0
        flattened_board = sum(b, [])
        for i in range(len(flattened_board) - 1):
            if i == 4:  # central tile
                if flattened_board[i] != 0:
                    sn += 1
            else:
                if flattened_board[i] + 1 != flattened_board[i + 1]:
                    sn += 2
        return sn

    return h2(board) + BOARD_SIZE * _score_sum(board)


def a_star(board: List[List[int]], heuristic):
    pass


if __name__ == '__main__':
    # r = generate_random_configuration(n=10)
    r = [[3, 1, 2],
         [6, 4, 5],
         [7, 0, 8]]
    # print(depth_first_search(r))
    # print(depth_first_search_limit(r, 100))
    # print(depth_iterative_search(r))
    print(h3(r))
