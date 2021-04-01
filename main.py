import heapq
import random
from typing import Tuple, List, Callable

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


def print_board(board: List[List[int]]) -> None:
    to_print = ''
    for i in range(BOARD_SIZE):
        to_print += ' | '.join(str(s) for s in board[i]) + '\n'
    print(to_print)


def move(board: List[List[int]], direction: str) -> None:
    i, j = get_white_tile(board)
    i_tmp = i
    j_tmp = j
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

    if i == i_tmp and j == j_tmp:
        raise ValueError('Tile 0 could not been moved.')


def generate_random_configuration(moves: int = 100) -> List[List[int]]:
    random_config = copy_board(FINAL_STATE)
    while random_config == FINAL_STATE:
        for k in range(moves):
            moved = False
            while not moved:
                try:
                    move(random_config, random.choice(DIRECTIONS))
                    moved = True
                except ValueError:
                    moved = False
    return random_config


def copy_board(board: List[List[int]]) -> List[List[int]]:
    new_board = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            new_board[i][j] = board[i][j]
    return new_board


def get_white_tile(board: List[List[int]]) -> Tuple[int, int]:
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                return i, j
    raise ValueError('Array does not contains 0.')


# Exercise 2

def breadth_first_search(board: List[List[int]]) -> Tuple[bool, int, int]:
    queue = [board]
    depth = 0
    nodes_visited = 0

    while queue:
        current_board = queue.pop(0)

        if current_board == FINAL_STATE:
            return True, depth, nodes_visited

        for direction in DIRECTIONS:
            try:
                board_copy = copy_board(current_board)
                move(board_copy, direction)
                queue.append(board_copy)
                nodes_visited += 1
            except ValueError:
                pass

        depth += 1

    return False, depth, nodes_visited


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

        for direction in DIRECTIONS:
            board_copy = copy_board(current_board)
            try:
                move(board_copy, direction)
                if board_copy not in seen:
                    stack.append((board_copy, depth + 1))
            except ValueError:
                pass

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

        if depth < limit:
            for direction in DIRECTIONS:
                board_copy = copy_board(current_board)
                try:
                    move(board_copy, direction)
                    if board_copy not in seen:
                        stack.append((board_copy, depth + 1))
                except ValueError:
                    pass
    return False, depth, nodes_visited


def depth_iterative_search(board: List[List[int]]) -> Tuple[bool, int, int]:
    found = False
    depth = 0
    nodes_visited = 0
    limit = 0
    while not found:
        limit += 1
        found, depth, nodes_visited = depth_first_search_limit(board, limit)
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


def a_star(board: List[List[int]], heuristic: Callable) -> Tuple[int, int]:
    p_queue = []
    heapq.heappush(p_queue, (0, board, 0))
    saved_costs = {repr(board): 0}
    nodes_visited = 0
    depth = 0

    while p_queue:
        priority, current_board, depth = heapq.heappop(p_queue)

        if current_board == FINAL_STATE:
            return depth, nodes_visited

        nodes_visited += 1

        for direction in DIRECTIONS:
          
            try:
                new_cost = saved_costs[repr(current_board)] + 1
                next_board = copy_board(current_board)
                move(next_board, direction)
                next_board_repr = repr(next_board)

                if next_board_repr not in saved_costs or new_cost < saved_costs[next_board_repr]:
                    saved_costs[next_board_repr] = new_cost
                    priority = new_cost + heuristic(next_board)
                    heapq.heappush(p_queue, (priority, next_board, depth + 1))
            except ValueError:
                pass

    return depth, nodes_visited


if __name__ == '__main__':
    m = 100
    print(f'Random configuration with {m} moves : ')
    random_board = generate_random_configuration(moves=m)
    print_board(random_board)

    # print('Breadth First Search :')
    # f, d, n = breadth_first_search(random_board)
    # print(f'Found : {f}\nDepth : {d}\nNodes visited : {n}\n')

    # print('Depth First Search :')
    # f, d, n = depth_first_search(random_board)
    # print(f'Found : {f}\nDepth : {d}\nNodes visited : {n}\n')

    # print('Depth First Search with limit :')
    # f, d, n = depth_first_search_limit(random_board, 100)
    # print(f'Found : {f}\nDepth : {d}\nNodes visited : {n}\n')

    # print('Depth Iterative Search with limit :')
    # f, d, n = depth_iterative_search(random_board)
    # print(f'Found : {f}\nDepth : {d}\nNodes visited : {n}\n')

    heuristics = [h1, h2, h3]
    for h in heuristics:
        h_name = getattr(h, '__name__', repr(h))
        print(f'A* using {h_name} :')
        d, n = a_star(random_board, h)
        print(f'Depth : {d}\nNodes visited : {n}\n')
