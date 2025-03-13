import math
from functools import lru_cache


class Discriminant:
    def __init__(self, num_a: int, num_b: int, num_c: int):
        self.num_a: str = num_a
        self.num_b: str = num_b
        self.num_c: str = num_c

    @lru_cache(maxsize=100)
    def count(self) -> object:
        self.num_d: str
        self.num_d = self.num_b * self.num_b - 4 * self.num_a * self.num_c
        if self.num_d > 0:
            x1 = (-self.num_b + math.sqrt(self.num_d)) / (2 * self.num_a)
            x2 = (-self.num_b - math.sqrt(self.num_d)) / (2 * self.num_a)
            return f"x1={x1}\nx2={x2}"
        if self.num_d == 0:
            x = (-self.num_b + math.sqrt(self.num_d)) / (2 * self.num_a)
            return f"x={x}"
        return f"Error.The discriminant cannot be less than 0."


if __name__ == "__main__":
    flsd = Discriminant(4,5,6)
    print(flsd.count())