from phone_regex import is_phone_number_without_regex


class TestIsPhoneNumberWithoutRegex:
    
    def test_valid_phone_number(self):
        assert is_phone_number_without_regex("415-555-4242") is True

    def test_invalid_phone_number_with_not_enough_characters(self):
        assert is_phone_number_without_regex("415-555-424") is False
    
    def test_invalid_phone_number_with_too_many_characters(self):
        assert is_phone_number_without_regex("4215-555-4242") is False
    
    def test_invalid_phone_number_without_hyphen(self):
        assert is_phone_number_without_regex("415 555 4242") is False
    
    def test_invalid_phone_number_containing_a_letter(self):
        assert is_phone_number_without_regex("415-A55-4242") is False
