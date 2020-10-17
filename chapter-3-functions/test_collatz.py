from collatz import collatz


def test_collatz():
    assert collatz(4) == 2
    assert collatz(1) == 4