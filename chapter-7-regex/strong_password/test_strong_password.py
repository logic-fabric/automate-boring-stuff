from strong_password import (
    contains_digit,
    contains_lowercase,
    contains_uppercase,
    is_strong_password,
)

class TestIsStrongPassword:

    def test_valid_password(self):
        assert is_strong_password("1234abAB") is True

    def test_contains_digit(self):
        assert contains_digit("ABCD-abcd") is False
    
    def test_contains_lowercase(self):
        assert contains_lowercase("ABCD-1234") is False

    def test_contains_uppercase(self):
        assert contains_uppercase("1234-abcd") is False

    def test_password_length(self):
        assert is_strong_password("1234") is False
