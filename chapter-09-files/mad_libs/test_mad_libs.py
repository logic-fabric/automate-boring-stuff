import os

from mad_libs import (
    ask_user_for_change_if_keyword,
    make_user_change_the_initial_sentence,
    write_user_sentence_in_text_file,

    INITIAL_SENTENCE,
    KEYWORDS,
    USER_INPUT,
    USER_SENTENCE,
    USER_SENTENCE_FILE,
)


class TestAskUserForChangeIfKeyWord:

    def test_no_change_if_word_is_not_a_keyword(self):
        word = "panda"
        
        assert any(keyword in word for keyword in KEYWORDS) is False
        assert ask_user_for_change_if_keyword(word) == word

    def test_correct_change_if_word_is_a_keyword(self):
        pass

    def test_correct_chnage_if_word_contains_a_keyword_with_punctuation(self):
        pass


class TestMakeUserChangeTheInitialSentence:

    def test_user_inputs_change_correctly_initial_sentence(self):
        pass


class TestWriteUserSentenceInTextFile:

    def test_user_text_file_is_created(self):
        write_user_sentence_in_text_file(USER_SENTENCE)
        
        assert USER_SENTENCE_FILE in os.listdir('.')

        os.unlink(USER_SENTENCE_FILE)

    def test_user_sentence_is_user_sentence_file_content(self):
        write_user_sentence_in_text_file(USER_SENTENCE)

        with open(USER_SENTENCE_FILE) as f:
            content = f.read()
            assert content == USER_SENTENCE
        
        os.unlink(USER_SENTENCE_FILE)

class TestMadLibs:

    def test_mad_libs_create_the_right_file(self):
        pass
        