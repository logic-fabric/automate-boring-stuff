import pytest

from collatz import collatz


def test_collatz_compute_well():
    assert collatz(4) == 2
    assert collatz(1) == 4

def test_collatz_raises_an_exception_without_a_non_null_positive_integer():
    with pytest.raises(ValueError):
        collatz(0)
    with pytest.raises(ValueError):
        collatz(-1)
    with pytest.raises(ValueError):
        collatz(True)
    with pytest.raises(ValueError):
        collatz(4.0)
    with pytest.raises(ValueError):
        collatz("NaN")
    with pytest.raises(ValueError):
        collatz([4])
    with pytest.raises(ValueError):
        collatz((4,))
    with pytest.raises(ValueError):
        collatz({4})
