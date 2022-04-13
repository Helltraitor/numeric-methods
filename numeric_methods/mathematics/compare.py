from decimal import Decimal
from fractions import Fraction
from math import isclose

from numeric_methods.mathematics import EPSILON


NUMBER = Decimal | float | Fraction


def compare(lhs: NUMBER, kind: str, rhs: NUMBER) -> bool:
    epsilon = EPSILON.with_context(lhs)
    return {
        "==": lambda: isclose(lhs, rhs, abs_tol=epsilon),
        "<=": lambda: (lhs < rhs) or isclose(lhs, rhs, abs_tol=epsilon),
        ">=": lambda: (lhs > rhs) or isclose(lhs, rhs, abs_tol=epsilon),
        "<": lambda: lhs < rhs,
        ">": lambda: lhs > rhs
    }[kind]()
