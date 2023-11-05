import csv
from fastDamerauLevenshtein import damerauLevenshtein

def get_list():
    with open('resources/data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        lines = {row[0] for row in reader}
    return lines      

def check_substring(string, word): 
    return string in word or word in string

def swapped_words(string, word):
    sorted_word1 = ''.join(sorted(string))
    sorted_word2 = ''.join(sorted(word))
    return sorted_word1 == sorted_word2

def check_typo(string): 
   lines = get_list()
   #first check if they have exactly same value 
   if string in lines:
       return (None,'No typo found')
   else: 
       for word in lines:
           if check_substring(string, word):
               # check if it is a substring
               return (word, 'Substring')
           else: 
           # then check swapped words             
            if swapped_words(string, word):
                return (word, 'Swapped words')
            else:
                # then check levenstein distance
                if damerauLevenshtein(string, word) < 2:
                    return (word, 'Levenstein distance')
                # if no then say this is not in the package list 
       return(None, 'Not in the package list')               