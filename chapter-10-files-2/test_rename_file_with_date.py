import os
from pathlib import Path

import pytest

from rename_files_with_date import (
    change_date_format_from_am_to_eu,
    change_name_with_date,
    rename_file_with_date,
    rename_files_with_date_in_folder,
)


TEST_FILE_CONTENT = "Test file successfully created."


class TestChangeDateFormatFromAmericanToFrench:

    def test_exchange_days_and_months(self):
        date = "10-23-2020"
        assert change_date_format_from_am_to_eu(date) == "23-10-2020"

    def test_return_error_message_if_invalid_date_given(self):
        date = "10/23/2020"
        assert change_date_format_from_am_to_eu(date) == f"{date} is not a valid american MM-DD-YYYY formated date."

        date = "13-23-2020"
        assert change_date_format_from_am_to_eu(date) == f"{date} is not a valid american MM-DD-YYYY formated date."

        date = "23 octobre 2020"
        assert change_date_format_from_am_to_eu(date) == f"{date} is not a valid american MM-DD-YYYY formated date."


class TestChangeNameWithDate:

    def test_concerned_name_is_correctly_changed(self):
        name = "test_name-10-23-2020.txt"
        assert change_name_with_date(name) == "test_name-23-10-2020.txt"

        name = "test_name-11-10-2020.txt"
        assert change_name_with_date(name) == "test_name-10-11-2020.txt"

    def test_concerned_name_with_two_dates_is_correctly_changed(self):
        name = "from_10-23-2020_to_10-25-2020.txt"
        assert change_name_with_date(name) == "from_23-10-2020_to_25-10-2020.txt"

    def test_unconcerned_fillename_stay_unchanged(self):
        name = "name_without_date.txt"
        assert change_name_with_date(name) == name


class TestRenameFileWithDate:

    def test_concerned_file_is_correctly_renamed(self):
        filename = "test_file-10-23-2020.txt"
        expected_filename = "test_file-23-10-2020.txt"

        path = Path.cwd() / filename
        with open(path, 'w') as f:
            f.write(TEST_FILE_CONTENT)

        rename_file_with_date(filename)
        files_in_current_folder = os.listdir()

        assert filename not in files_in_current_folder
        assert expected_filename in files_in_current_folder

        path = Path.cwd() / expected_filename
        with open(path, 'r') as f:
            expected_file_content = f.read()
        
        assert expected_file_content == TEST_FILE_CONTENT

        os.unlink(path)

    def test_unconcerned_file_is_unchanged(self):
        filename = "test_file_without_date.txt"

        path = Path.cwd() / filename
        with open(path, 'w') as f:
            f.write(TEST_FILE_CONTENT)

        rename_file_with_date(filename)
        files_in_current_folder = os.listdir()

        assert filename in files_in_current_folder

        with open(path, 'r') as f:
            expected_file_content = f.read()
        
        assert expected_file_content == TEST_FILE_CONTENT

        os.unlink(path)


class TestRenameFilesWithDateInFolder:

    def test_rename_two_files_with_date_and_one_without(self):

        changing_filenames = [
            {
                'initial': "test_name-11-10-2020.txt",
                'expected': "test_name-10-11-2020.txt",
            },
            {
                'initial': "from_10-23-2020_to_10-25-2020.txt",
                'expected': "from_23-10-2020_to_25-10-2020.txt",
            },
        ]
        unchanging_filename = "test_file_without_date.txt"

        for filename in changing_filenames:
            path = Path.cwd() / filename['initial']
            with open(path, 'w') as f:
                f.write(TEST_FILE_CONTENT)

        path = Path.cwd() / unchanging_filename
        with open(path, 'w') as f:
            f.write(TEST_FILE_CONTENT)

        rename_files_with_date_in_folder(Path.cwd())
        files_in_current_folder = os.listdir()

        for filename in changing_filenames:
            assert filename['initial'] not in files_in_current_folder
            assert filename['expected'] in files_in_current_folder

            path = Path.cwd() / filename['expected']
            with open(path, 'r') as f:
                expected_file_content = f.read()
            
            assert expected_file_content == TEST_FILE_CONTENT

        assert unchanging_filename in files_in_current_folder

        path = Path.cwd() / unchanging_filename
        with open(path, 'r') as f:
            expected_file_content = f.read()
            
        assert expected_file_content == TEST_FILE_CONTENT

        for filename in changing_filenames:
            os.unlink(filename['expected'])

        os.unlink(unchanging_filename)
