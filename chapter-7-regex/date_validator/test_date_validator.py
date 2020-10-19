from date_validator import (
    is_leap_year,
    is_valid_date,
    is_valid_date_format,
)


class TestIsLeapYear:
    
    def test_leap_years(self):
        assert is_leap_year(2000) is True
        assert is_leap_year(2020) is True

    def test_non_leap_years(self):
        assert is_leap_year(2019) is False
        assert is_leap_year(2100) is False


class TestIsValidDate:
    
    def test_valid_dates(self):
        assert is_valid_date("19/10/2020") is True

        assert is_valid_date("29/02/2020") is True
        assert is_valid_date("29/02/2000") is True
        

    def test_invalid_dates(self):
        assert is_valid_date("19-10-2020") is False
        assert is_valid_date("19.10.2020") is False
        assert is_valid_date("19 10 2020") is False

        assert is_valid_date("31/02/2019") is False
        assert is_valid_date("00/10/2020") is False
        assert is_valid_date("32/10/2020") is False

        assert is_valid_date("19/00/2020") is False
        assert is_valid_date("19/13/2020") is False

        assert is_valid_date("29/02/2019") is False
        assert is_valid_date("29/02/2100") is False


class TestIsValidDateFormat:

    def test_valid_date_strings(self):
        assert is_valid_date_format("19/10/2020") is True

    def test_invalid_date_separator(self):
        assert is_valid_date_format("19-10-2020") is False
        assert is_valid_date_format("19.10.2020") is False
        assert is_valid_date_format("19 10 2020") is False

    def test_invalid_day_number(self):
        assert is_valid_date_format("00/10/2020") is False
        assert is_valid_date_format("32/10/2020") is False

    def test_invalid_month_number(self):
        assert is_valid_date_format("19/00/2020") is False
        assert is_valid_date_format("19/13/2020") is False

    def test_invalid_year_number(self):
        assert is_valid_date_format("19/10/20") is False
