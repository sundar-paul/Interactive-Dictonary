import json
from difflib import get_close_matches

data=json.load(open('076 data.json'))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8))>0:
        yn=input("Did u mean %s instead? Enter Y if yes, N of no: "% get_close_matches(word, data.keys(),cutoff=0.8)[0])
        if yn=='Y' or yn=='y':
            return data[get_close_matches(word, data.keys(),cutoff=0.8)[0]]
        elif yn=='N' or yn=='n':
            return "The word doesn't exist.Please check it."
        else:
            return 'We did not understand your entry'
    else:
        return "The word doesn't exist.Please check it."

word=input('Enter Word: ')
output=translate(word)

if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)