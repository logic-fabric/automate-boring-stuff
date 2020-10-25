"""Script that opens Google Map with the adress given through command line.
"""

import sys
import webbrowser


if __name__ == '__main__':
    if len(sys.argv) > 1:
        address = " ".join(sys.argv[1:])
        print(address)
    else:
        address = ""

    url = f'https://google.com/maps/place/{address}'
    webbrowser.open(url)
