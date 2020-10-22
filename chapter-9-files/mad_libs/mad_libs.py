"""Implement a function that ask user to complete a sentence by replacing the words ADJECTIVE, NOUN, ADVERB and VERB.
The sentence created by the user is thend saved in a USER_SENTENCE_FILE.
"""


INITIAL_SENTENCE = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."

USER_INPUT = ['silly', 'chandelier', 'screamed', 'truck']
USER_SENTENCE = "The {} panda walked to the {} and then {}. A nearby {} was unaffected by these events.".format(*USER_INPUT)


KEYWORDS = [
    'ADJECTIVE',
    'ADVERB',
    'NOUN',
    'VERB',
]
USER_SENTENCE_FILE = 'user_sentence.txt'


def ask_user_for_change_if_keyword(word):
    for keyword in KEYWORDS:
        if keyword in word:
            user_input = input(f"Enter a {keyword.lower()}: ")
            return word.replace(keyword, user_input)
    
    return word

def make_user_change_the_initial_sentence(sentence):
    words = sentence.split()
    changed_words = []

    for word in words:
        changed_word = ask_user_for_change_if_keyword(word)
        changed_words.append(changed_word)

    return " ".join(changed_words)

def write_user_sentence_in_text_file(user_sentence):
    with open(USER_SENTENCE_FILE, 'w') as f:
        f.write(user_sentence)

def mad_libs(sentence):
    user_sentence = make_user_change_the_initial_sentence(sentence)
    write_user_sentence_in_text_file(user_sentence)

    print(
        f'"{user_sentence}"" has been successfully saved in {USER_SENTENCE_FILE}.'
    )


if __name__ == '__main__':
    mad_libs(INITIAL_SENTENCE)
