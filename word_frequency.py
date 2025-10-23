#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

user_sentence = input("Enter a sentence: ")

while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")
    
unique = []
frequencies = []

splitted_sentence = user_sentence.split()

for word in splitted_sentence:
    clean_word = re.sub(r'[^\w]', '', word.lower()) #checks for clean words
    if clean_word in unique:
        i = unique.index(clean_word) #assigns value to the index of duplicate word
        frequencies[i] += 1  #incerements that assigned index
    else:
        unique.append(clean_word)
        frequencies.append(1)

#used copilot
for i in range(len(unique)):
    print(f"{unique[i]}: {frequencies[i]}")