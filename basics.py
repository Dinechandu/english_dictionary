import json
from difflib import get_close_matches

#Open and Loading from Json File
data=json.load(open('data.json')) 

#Function to Search for the given word
def search(word_means):
    if word_means in data:                #Condition to check the existence of user_input
        return data[word_means]
    elif word_means.title() in data:      #Condition to check user_input ,if the JSON file has words that start with a capital letter (e.g. Delhi or Texas)
        return data[word_means.title()]
    elif word_means.upper() in data:      #Condition to check for Acronyms such as USA or NATO in JSON file
        return data[word_means.upper()]
    elif len(get_close_matches(word_means,data.keys())) > 0:      #Check if word is valid to avoid traceback error before reading from database
        res=input('You meant %s ?, If Yes Press Y Else Press N:- ' %get_close_matches(word_means,data.keys())[0])   #Suggesting the correct word from the mispelled user_input
        if res =='Y'or res=='y':
            return data[get_close_matches(word_means,data.keys())[0]]
        elif res=='N' or res=='n':
            return "Sorry %s doesn't match any other words in the dictionary. Check spelling and try again"%word_means
        else:
            return 'Sorry that wasn''t one of the options.'
    else:
        return "Doesn't match any words in dictionary. Check spelling"

#ask for user input
word=input("Enter the word: ")

#makes all lowercase and proceeds to function call
ans=search(word.lower())

#convert list output to string
if type(ans)==list:
    for i in ans:
        print(i)
else:
    print(ans)
        
