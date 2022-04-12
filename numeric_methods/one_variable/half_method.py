from decimal import Decimal
from fractions import Fraction
from math import log2
from typing import Generator

from numeric_methods.language import TRANSLATE
from numeric_methods.mathematic import compare, convert, widest_type


NUMBER = Decimal | float | Fraction


def half_method(function, a_0: NUMBER, b_0: NUMBER, epsilon: NUMBER) -> Generator[tuple[NUMBER] | NUMBER, None, None]:
    # Type normalization
    Number = widest_type(a_0, b_0, epsilon)
    a_0 = convert(a_0, Number)
    b_0 = convert(b_0, Number)
    epsilon = convert(epsilon, Number)

    if not compare(function(a_0) * function(b_0), "<", Number(0)):
        raise ArithmeticError(f"Value of function({a_0}) * function({a_0}) must be less then zero")

    a = a_0
    b = b_0
    step = 0
    last_step = int(log2((b_0 - a_0) / epsilon))
    while True:
        step += 1
        x = (a + b) / Number(2)
        y = function(x)

        yield step, a, b, x, y

        if compare(y, "==", Number(0)):
            yield x
            return
        elif compare(y, "<", Number(0)):
            a = x
        elif compare(y, ">", Number(0)):
            b = x

        if step > last_step:
            yield x
            return
