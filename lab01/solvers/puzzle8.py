from .search import bfs


GOAL = (1, 2, 3, 4, 0, 5, 6, 7, 8)
DIRECTIONS = (
    ("空格上移", -1, 0),
    ("空格下移", 1, 0),
    ("空格左移", 0, -1),
    ("空格右移", 0, 1),
)


def inversions(state):
    tiles = [tile for tile in state if tile != 0]
    return sum(
        left > right
        for index, left in enumerate(tiles)
        for right in tiles[index + 1:]
    )


def is_solvable(state):
    if len(state) != 9 or set(state) != set(range(9)):
        raise ValueError("棋盘必须恰好包含一次 0 到 8")
    return inversions(state) % 2 == inversions(GOAL) % 2


def moves(state):
    blank = state.index(0)
    row, col = divmod(blank, 3)

    for action, dr, dc in DIRECTIONS:
        next_row, next_col = row + dr, col + dc
        if 0 <= next_row < 3 and 0 <= next_col < 3:
            other = next_row * 3 + next_col
            next_state = list(state)
            next_state[blank], next_state[other] = next_state[other], next_state[blank]
            yield action, tuple(next_state)


def solve(start):
    start = tuple(start)
    if not is_solvable(start):
        return None
    return bfs(start, lambda state: state == GOAL, moves)