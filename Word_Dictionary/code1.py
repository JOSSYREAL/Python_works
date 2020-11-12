from difflib import get_close_matches
#Joseph dictionary

#import json to load access the json file
import json
#use the load and open keyword to access the json file
data = json.load(open("data.json"))

'''dictionary search to output the meaning of words'''
def search(word):
    if word.upper() in data:
        return data[word.upper()]
    elif word.lower() in data:
        return data[word.lower()]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())[0]):
        print("Not found!, do you mean %s instead" %get_close_matches(word, data.keys())[0])
        decision = input("Type y for yes or n for no: ")
        if decision == "y" or "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decision == "n" or "N":
            return "Word not in dic"
        else:
            return "Wrong input"

    else:
        return "Word not in dic"

word = input("Enter word to check meaning: ")
output = search(word)
if type(output) == list:
    for word in output:
        print(word)
else:
    print(output)

def translate(word):
    if word.upper() in data:
        return data[word.upper()]
    elif word.lower() in data:
        return data[word.lower()]
    elif word.title() in data:
        return data[word.title()]
    
    elif len(get_close_matches(word, data.keys())[0]):
        print("Not found!, do you mean %s instead" %get_close_matches(word, data.keys())[0])
