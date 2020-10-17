"""Implement a function to compute the sequence of the Collatz conjecture ("conjecture de Syracuse" in french):

1. the sequence starts with a non null integer
2. if a number N is even, its successor is N / 2
3. else, its successor is 3 * N + 1

The conjecture says that this sequence will always end in the cycle (1, 4, 2).
"""


def collatz(n):
    return 3 * n + 1 if n % 2 else n // 2


if __name__ == "__main__":
    pass