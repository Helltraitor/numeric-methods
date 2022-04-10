from fractions import Fraction
from decimal import Decimal


class Epsilon:
    def __init__(self):
        self.decimal = Decimal("1e-9")
        self.float = float("1e-9")
        self.fraction = Fraction("1e-9")

    def set(self, epsilon: str) -> bool:
        try:
            _decimal = Decimal(epsilon)
            _float = float(epsilon)
            _fraction = Fraction(epsilon)
        except Exception:
            return False

        self.decimal = _decimal
        self.float = _float
        self.fraction = _fraction
        return True

    def restore(self):
        self.set("1e-9")

    def with_context(self, number: int | float | Decimal | Fraction) -> float | Decimal | Fraction:
        if isinstance(number, Decimal):
            return self.decimal
        if isinstance(number, (int, float)):
            return self.float
        if isinstance(number, Fraction):
            return self.fraction


EPSILON = Epsilon()
