from pig_latin import pig_latin, pig_latin_sentence

COMPLEX_SENTENCE = "My name is AL SWEIGART and I am 4,000 years old."
COMPLEX_PIG_LATIN_SENTENCE = "Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay."


def test_pig_latin_an_empty_string():
    assert pig_latin("") == ""

def test_pig_latin_each_word_of_the_complex_sentence():
    assert pig_latin("My") == "Ymay"
    assert pig_latin("name") == "amenay"
    assert pig_latin("is") == "isyay"
    assert pig_latin("AL") == "ALYAY"
    assert pig_latin("SWEIGART") == "EIGARTSWAY"
    assert pig_latin("I") == "Iyay"
    assert pig_latin("4,000") == "4,000"
    assert pig_latin("old.") == "oldyay."
    assert pig_latin("cold.") == "oldcay."

def test_pig_latin_complex_sentence():
    assert pig_latin_sentence(COMPLEX_SENTENCE) == COMPLEX_PIG_LATIN_SENTENCE
