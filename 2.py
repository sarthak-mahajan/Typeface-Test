# input for this file is 2 command line arguments, the first argument is the word to search for and the second argument is the nane of the file in which it needs to be searched
#the output is a list of all names which match with the input
# the input file contains a list of word, each word separated by a new line

import jellyfish

from fuzzywuzzy import fuzz
from sys import argv


in_str = argv[1]
file_name = argv[2]

listofwords = open(file_name).readlines()

code1 = jellyfish.soundex(in_str)

score_word = {}

for i in listofwords:
    i=i.strip()
    code2 = jellyfish.soundex(i)
    rat = fuzz.ratio(code1,code2)
    rat2 = fuzz.ratio(in_str,i)
    if rat == 100 :
        score_word[i] = rat
    else :
        score_word[i] = (rat+rat2)/2



sorted_score =  {k: v for k, v in sorted(score_word.items(), key=lambda item: item[1], reverse=True)}


if100 = False
count = 0
for i in sorted_score:
    if sorted_score[i] == 100:
        if100 = True
    count += 1
    if count >= 2 :
        break

for i in sorted_score:
    if if100 :
        if sorted_score[i] == 100:
            print(i)
        else :
            break
    else :
        if sorted_score[i] >= 61 :
            print (i)
        else :
            print ("no match found")
            break