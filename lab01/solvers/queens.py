from time import perf_counter

from .search import SolveResult


def moves(placement, n):
    row = len(placement)
    if row == n:
        return

    for col in range(1, n + 1):
        if all(
            col != old_col and abs(col - old_col) != row - old_row
            for old_row, old_col in enumerate(placement)
        ):
            yield f"第 {row + 1} 行放第 {col} 列", placement + (col,)


def solve(n=8):
    if n < 1:
        raise ValueError("n 必须为正整数")

    started = perf_counter()
    expanded = 0
    count = 0
    first_path = None

    def backtrack(placement, path):
        nonlocal expanded, count, first_path
        if len(placement) == n:
            count += 1
            if first_path is None:
                first_path = path.copy()
            return

        expanded += 1
        for action, next_state in moves(placement, n):
            path.append((action, next_state))
            backtrack(next_state, path)
            path.pop()

    backtrack((), [(None, ())])
    if first_path is None:
        return None
    return SolveResult(first_path, expanded, (perf_counter() - started) * 1000, count)