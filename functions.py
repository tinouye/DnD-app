import random
import json
from character import Character
from custom_exceptions import BadCommand 

def backend_roll(num, die):
    sum = 0
    print("Rolling {}d{}".format(num, die))

    for i in range(num):
        new_roll = random.randint(1, die)
        sum += new_roll
        print(new_roll)
    
    print("Sum: {}".format(sum))


def roll(word_list):
    error_msg = "Roll syntax is 'roll XdY' where X and Y are numbers (4, 6, 8, 10, 12, 20)"

    if len(word_list) != 1 or type(word_list[0]) is not str:
        print(error_msg)
    
    else:
        split_keyword = word_list[0].split('d')
        if len(split_keyword) != 2:
            print(error_msg)
        else:
            try:
                num = int(split_keyword[0])
                die = int(split_keyword[1])
                backend_roll(num, die)
            except ValueError:
                print(error_msg)


def backend_load_char(filename):
    loadfile = open(f"{filename}.json", "r")
    loaded_json = loadfile.read()
    return Character(**json.loads(loaded_json))


def load_char(word_list):
    filename = " ".join(word_list)
    return backend_load_char(filename)