import pytest

from factorial import factorial, ARGUMENT_ERROR_MESSAGE


class TestFactorial:

    def test_factorial_is_1_for_0_and_1(self):
        assert factorial(0) == 1
        assert factorial(1) == 1

    def test_factorial_5_is_120(self):
        assert factorial(5) == 120

    def test_factorial_raises_exception_with_negative_integers(self):
        with pytest.raises(ValueError) as e:
            factorial(-1)

        assert str(e.value) == ARGUMENT_ERROR_MESSAGE
    
    def test_factorial_raises_exception_with_floats_if_decimal_part(self):
        assert factorial(5.0) == 120

        with pytest.raises(ValueError) as e:
            factorial(5.1)

        assert str(e.value) == ARGUMENT_ERROR_MESSAGE

    def test_factorial_raises_exception_with_non_numeric_arguments(self):
        with pytest.raises(TypeError) as e:
            factorial("five")

        assert str(e.value) == ARGUMENT_ERROR_MESSAGE
