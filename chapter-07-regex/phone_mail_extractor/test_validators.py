from phone_mail_extractor import (
    is_valid_mail,
    is_valid_phone_number,
)


class TestIsValidPhoneNumber:

    def test_valid_phone_numbers(self):
        assert is_valid_phone_number('421-421-4242') is True
        assert is_valid_phone_number('421.421.4242') is True
        assert is_valid_phone_number('421 421 4242') is True

        assert is_valid_phone_number('(421)-421-4242') is True
        assert is_valid_phone_number('(421).421.4242') is True
        assert is_valid_phone_number('(421) 421 4242') is True

        assert is_valid_phone_number('421-4242') is True
        assert is_valid_phone_number('421.4242') is True
        assert is_valid_phone_number('421 4242') is True

        assert is_valid_phone_number('421-4242') is True
        assert is_valid_phone_number('421.4242') is True
        assert is_valid_phone_number('421 4242') is True

    def test_invalid_phone_numbers(self): 
        assert is_valid_phone_number('AAA-BBB-CCCC') is False
        assert is_valid_phone_number('4214214242') is False
        assert is_valid_phone_number('421/421/4242') is False


class TestIsValidMail:

    def test_valid_mails(self):
        assert is_valid_mail('john@example.com') is True
        assert is_valid_mail('john.doe@example.com') is True
        assert is_valid_mail('john.doe42@example.com') is True

    def test_invalid_maisl(self):
        assert is_valid_mail('john@example') is False
        assert is_valid_mail('john.doe.example.com') is False
