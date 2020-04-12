from difflib import get_close_matches
import json

data = json.load(open('original.json'))

def tranlate(word):
    word = word.lower()
    if word in data:
        return data[word]


    elif word.title() in data:
        return data[word.title()]


    elif word.upper() in data:
        return data[word.upper()]


    elif len(get_close_matches(word,data.keys())) > 0:
        print("did you mean %s instead "%get_close_matches(word,data.keys())[0])
        decide = input("press y for yes or n for no")
        if decide == 'y' or decide == 'Y':
            return data[get_close_matches(word,data.keys())[0]]
        elif decide == 'n' or decide =='N':
            x= input("if you want to search again press y: ")
            if x=='y' or x=='Y':

                start(x)
            else:
                exit()
        else:
            print("you have Entered wrong word please check it again..")
            x= input("if you want to search again press y: ")
            if x=='y' or x=='Y':
                start(x)
            else:
                exit()



    else:
        print("you have Entered wrong word please check it again..")
        x= input("if you want to search again press y: ")
        if x=='y' or x=='Y':
            start(x)
        else:
            exit()



def start(x):
    word = input("enter the word ,you want to search : ")
    output = tranlate(word)
    if type(output) == list:
        for item in output:
            print("\n*",item)
            x= input("\nif you want to search again press y: ")
            if x=='y' or x=='Y':
                start(x)
            else:
                exit()
    else:
        print(output)

#here program is start
x = 'y'
if x=='y' or x=='Y':
    start(x)
