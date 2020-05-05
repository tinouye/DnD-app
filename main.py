import functions
import api
from character import Character

def parse_input(inputstr):
    """
    Parse the input
    """
    word_list = inputstr.split()

    if word_list[0] == 'roll':
        functions.roll(word_list[1:])

    elif word_list[0] == 'search':
        api.search(word_list[1:])

    elif word_list[0] == 'load':
        return functions.load_char(word_list[1:])


if __name__ == "__main__":
    loaded_char = None
    inputstr = ""

    while inputstr != "quit":
        inputstr = input("\n\nEnter command: ")
        print("")
        output = parse_input(inputstr)
        if type(output) == Character:
            loaded_char = output