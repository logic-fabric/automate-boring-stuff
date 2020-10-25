"""Implement a function to compute the sequence of the Collatz conjecture ("conjecture de Syracuse" in french):

1. the sequence starts with a non null positive integer
2. if a number N is even, its successor is N / 2
3. else, its successor is 3 * N + 1

The conjecture says that this sequence will always end in the cycle (1, 4, 2).
"""


def collatz(n):
    if type(n) != int or n < 1:
        raise ValueError(
            "The collatz function needs a non null positive integer."
        )
    else:
        return 3 * n + 1 if n % 2 else n // 2


if __name__ == "__main__":
    
    for starting_integer in range(1, 21):
        n = starting_integer
        sequence = [n]

        while n != 1:
            n = collatz(n)
            sequence.append(n)

        output = " ".join([str(n) for n in sequence])
        print(f"Collatz conjecture verified with {starting_integer}:")
        print(output)
