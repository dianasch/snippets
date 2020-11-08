"""A Markov chain generator that can create random song snippets."""

from random import choice

import sys

# CODE BELOW FOR TESTING PURPOSES
# file_name = sys.argv[1]

# def open_and_read_file(file_name):
#     """Take file path as string; return text as string.
#     Takes a string that is a file path, opens the file, and turns
#     the file's contents as one string of text.
#     """

#     # your code goes here
#     file = open(file_name)
#     text = file.read()
#     return text

def make_chains(text):
    """Take input text as string; return dictionary of Markov chains."""

    # Strip trailing whitespace and remove `(, )`` chars from text
    # Set variable `words` to list of split text
    
    words = text.replace('(', ' ').replace(')', ' ').replace('"', ' ').replace('.', ' ').strip().split()
    
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