"""Implement a clipboard to print preset sentences with keywords passed in command line.
"""

import sys


PRESET_SENTENCES = {
    'agree': "Yes, I agree. That sounds find to me.",
    'busy': "Sorry, we will do this later, this week or next week.",
    'upsell': "Would you consider making this a monthly donation.",
}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Command example: 'python multiclipboard.py [keyphrase]'")
        sys.exit()
    
    clipboard = []
    for keyword in sys.argv[1:]:
        sentence = PRESET_SENTENCES.get(keyword)

        if sentence is not None:
            clipboard.append(sentence)
    
    print("\n".join(clipboard))
