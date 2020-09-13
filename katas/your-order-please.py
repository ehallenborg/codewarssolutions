import operator

def order(sentence):
    sentence = sentence.split()
    ordered = ""
    numbers = {"1":"NONE", "2":"NONE", "3":"NONE", "4":"NONE", "5":"NONE", "6":"NONE", "7":"NONE", "8":"NONE", "9":"NONE", }

    for word in sentence:
        for char in word:
            if(char.isdigit() and int(char) <= 9):
                numbers[char] = word
    numbers = sorted(numbers.items())

    for s in numbers:
        if(s[1] != "NONE"):
            ordered = ordered + s[1]+" "
    ordered = ordered[:-1]
    
    return ordered
