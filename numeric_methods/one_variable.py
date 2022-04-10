from decimal import Decimal
from fractions import Fraction
from math import log2
from typing import Generator

from numeric_methods.language import TRANSLATE
from numeric_methods.mathematic import compare


NUMBER = Decimal | float | Fraction


def half_method(function, a_0: NUMBER, b_0: NUMBER, epsilon: NUMBER) -> Generator[tuple[NUMBER] | NUMBER, None, None]:
    Number = type(a_0)
    if not compare("<", function(a_0) * function(b_0), Number(0)):
        raise ArithmeticError(f"Value of function({a_0}) * function({a_0}) must be less then zero")

    a = a_0
    b = b_0
    step = 0
    last_step = int(log2((b_0 - a_0) / epsilon))
    while True:
        step += 1
        half = (a + b) / Number(2)
        x = function(half)

        yield step, a, b, half, x

        if compare(x, "==", Number(0)):
            yield half
            return
        elif compare(x, "<", Number(0)):
            a = half
        elif compare(x, ">", Number(0)):
            b = half

        if step > last_step:
            yield half
            return
