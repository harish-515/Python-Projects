import json
from difflib import get_close_matches

data = json.load(open("resources/data.json"))

def get_the_meaning(w):
    w = w .lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        word_matched = input("Did you mean %s instead? Enter Y if yes or N if no to continue: " %  get_close_matches(w,data.keys())[0]).lower() 
        if word_matched.lower() == "y" :
            return data[get_close_matches(w,data.keys())[0]]
        elif word_matched.lower() == "n" :
            return "The word dosn't exist. Please double check it"
        else:
            return "We didn't understand your entry."        
    else:
        return "The word dosn't exist. Please double check it"    
 
word = input("Enter a word: ") 
output = get_the_meaning(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)            