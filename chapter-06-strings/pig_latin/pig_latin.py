"""Implement a function that translates a text in the silly Pig Latin language:
- if a word begins by a vowel, 'yay' is added to the end
- if a word begins by a consonant or a consonant cluster, that consonant or cluster is moved to the end of the word followed by 'ay'
"""


def pig_latin(word):
    if word == "":
        return ""

    if not word[0].isalpha():
        return word

    if word[0] in "aeiouy":
        if word[-1].isalpha():
            return word + "yay"    
        
        return word[:-1] + "yay" + word[-1]

    if word[0] in "AEIOUY":
        if word[-1].isalpha():
            return "Iyay" if word == "I" else word + "YAY"

        return word[:-1] + "YAY" + word[-1]
    
    consonant_cluster = ""
    pig_latin_start = word

    while pig_latin_start and (not pig_latin_start[0] in "aeiouyAEIOUY"):
        consonant_cluster += pig_latin_start[0]
        pig_latin_start = pig_latin_start[1:]
    
    if word.isupper():
        if word[-1].isalpha():
            return pig_latin_start + consonant_cluster + "AY"

        return pig_latin_start[:-1] + consonant_cluster + "AY" + word[-1]

    elif word[0].isupper():
        if word[-1].isalpha():
            return pig_latin_start.capitalize() + consonant_cluster.lower() + "ay"

        return pig_latin_start[:-1].capitalize() + consonant_cluster.lower() + "AY" + word[-1]
        
    else:
        if word[-1].isalpha():
            return pig_latin_start + consonant_cluster + "ay"
        
        return pig_latin_start[:-1] + consonant_cluster + "ay" + word[-1]

def pig_latin_sentence(text):
    return " ".join(pig_latin(word) for word in text.split())


if __name__ == "__main__":
    pass
