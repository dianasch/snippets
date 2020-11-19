"""A Markov chain generator that can create random song snippets."""

from random import choice
from collections import Counter

import sys
import re


# CODE BELOW FOR TESTING PURPOSES
# file_name = sys.argv[1]

def open_and_read_file(file_name):
    """Take file path as string; return text as string.
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(file_name)
    text = file.read()
    return text

def make_chains(text):
    """Take input text as string; return dictionary of Markov chains."""

    # Strip trailing whitespace and remove `(, )`` chars from text
    # Set variable `words` to list of split text
    
    words = text.replace('(', ' ').replace(')', ' ').replace('"', ' ').replace('.', ' ').replace('[', ' ').replace(']', ' ').replace(",", " ").strip(" ").split()
    
    # Set variable `chains` to empty dictionary
    chains = {}

    # Loop through a range the length of words - 2
    for i in range(len(words) - 2):

        # Set variable `key` to a tuple of the words at index i and i + 1
        key = (words[i], words[i + 1])

        # Set variable `value` to the word at index i + 2,
        # the next word after the key
        value = words[i + 2]
        
        # If key not in chains, set key value to empty list
        if key not in chains.keys():
            chains[key] = []

        # If key is in chains, append value to list stored at key
        chains[key].append(value)
            
    return chains


def make_text(chains):
    """Return random text from chains."""

    #Set variable `keys` to keys in dict
    keys = chains.keys()

    #Set variable `key` to a random tuple from keys
    key = choice(list(keys))

    # Set variable `words` to list with key tuple
    words = [key[0].capitalize(), key[1]]

    # Limit random text length to 60
    while len(words) < 60:

        # Set variable `word` to a randomly chosen word from
        # the list stored at current key
        word = choice(chains[key])

        # Add that word to the list of Markov text
        words.append(word)

        # Set new key to a tuple of the second to last and last words in list
        key = (words[-2], words[-1])

    #Return joined list of words
    return " ".join(words)

# CODE BELOW FOR TESTING
# # Open the file and turn it into one long string
# input_text = open_and_read_file(file_name)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)


f = open_and_read_file('folklore.txt')
f2 = open_and_read_file('1989.txt')
f3 = open_and_read_file('Lover.txt')
f4 = open_and_read_file('Fearless.txt')
f5 = open_and_read_file('reputation.txt')
f6 = open_and_read_file('Speak Now.txt')
f7 = open_and_read_file('Taylor Swift.txt')
f8 = open_and_read_file('Red.txt')

def most_common(text):

    # Remove certain punctuation from album lyrics
    remove = text.lower().replace('?', ' ').replace('(', ' ').replace(')', ' ').replace(',', ' ')

    # Regex to find words
    clean_text = re.sub("^\w\d'\s]+",' ', remove)

    # List of clean words split into a list
    words = clean_text.strip().split()

    # Set of words that are too common to include in chart
    remove_set = set(['the', 'and','to', 'a', 'in', 'of', 'on'])

    # List of tuples with first item as word, second item as word count
    # Return 22 most common words in the album to accommodate for additional
    # words if all `remove` words appear in most common words
    # The desired result is a list of 15 most common words
    common = Counter(words).most_common(22)

    # Set variable `labels` to empty list to keep track of most common words
    # Labels for bar graph
    labels = []

    # Set variable `data` to empty list to keep track of num of occurrences
    # of most common words
    # Data for bar graph
    data = []

    # Loop through each word in `common`
    for word in common:

        # Limit top 15 words
        if len(labels) < 15:

            # If word is not in set of words to remove
            if word[0] not in remove_set:

                # Add capitalized word to list of labels
                labels.append(word[0].capitalize())

                # Add num of occurrences to list of data
                data.append(word[1])

    return tuple([labels, data])


# Code below to find 20 most unique words in an album
# Not currently implemented in app, but available for future use

# def least_common(text):

#     remove = text.lower().replace('?', ' ').replace('(', ' ').replace(')', ' ').replace(',', ' ')
#     clean_text = re.sub("^\w\d'\s]+",' ', remove)
#     words = clean_text.strip().split()

#     return Counter(words).most_common()[-19:]