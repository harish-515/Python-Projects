
def sentance_maker(phrase):
    introgative_words = ("how","what","why")
    capitalize = phrase.capitalize()
    if phrase.startswith(introgative_words):
        return "{}?".format(capitalize)
    else:
        return "{}.".format(capitalize)    

results = []

while True:
    user_input = input("Enter a statement: ")
    if user_input == "\end":
        break
    else:
        results.append(sentance_maker(user_input))

print(" ".join(results))        
