import json
import difflib
from difflib import SequenceMatcher 

d = enchant.Dict("en_US")
data = json.load(open("data.json"))

def check_word_in_file(arg):
    try:
        return print(data[arg])
    except KeyError:
        d.check(arg)
        return print(d.suggest(arg))

def main():
    request = input("Enter a word: ").lower()
    check_word_in_file(request)

main()
