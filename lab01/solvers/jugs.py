from math import gcd

from .search import bfs


OPERATIONS = ("装满A", "装满B", "倒空A", "倒空B", "A倒向B", "B倒向A")


def is_solvable(cap_a, cap_b, target):
    if cap_a <= 0 or cap_b <= 0 or target < 0:
        raise ValueError("杯容量必须是正整数，目标水量不能为负")
    return target <= max(cap_a, cap_b) and target % gcd(cap_a, cap_b) == 0


def moves(state, cap_a, cap_b, order=OPERATIONS):
    a, b = state
    from_a = min(a, cap_b - b)
    from_b = min(b, cap_a - a)

    candidates = {
        "装满A": (cap_a, b),
        "装满B": (a, cap_b),
        "倒空A": (0, b),
        "倒空B": (a, 0),
        "A倒向B": (a - from_a, b + from_a),
        "B倒向A": (a + from_b, b - from_b),
    }
    for action in order:
        next_state = candidates[action]
        if next_state != state:
            yield action, next_state


def solve(cap_a=3, cap_b=5, target=4, order=OPERATIONS):
    order = tuple(order)
    if len(order) != len(OPERATIONS) or set(order) != set(OPERATIONS):
        raise ValueError("order 必须包含六个不同的操作")
    if not is_solvable(cap_a, cap_b, target):
        return None

    return bfs(
        (0, 0),
        lambda state: target in state,
        lambda state: moves(state, cap_a, cap_b, order),
    )