# """A Markov chain generator that can tweet random messages."""

# import sys
# from random import choice
# import os



# def open_and_read_file(filenames):
#     """Take list of files. Open them, read them, and return one long string."""

#     body = ''
#     for filename in filenames:
#         text_file = open(filename)
#         body = body + text_file.read()
#         text_file.close()

#     return body


# def make_chains(text_string):
#     """Take input text as string; return dictionary of Markov chains."""

#     chains = {}

#     words = text_string.split()
#     for i in range(len(words) - 2):
#         key = (words[i], words[i + 1])
#         value = words[i + 2]

#         if key not in chains:
#             chains[key] = []

#         chains[key].append(value)

#     return chains


# def make_text(chains):
#     """Take dictionary of Markov chains; return random text."""

#     keys = list(chains.keys())
#     key = choice(keys)

#     words = [key[0], key[1]]
#     while key in chains:
#         # Keep looping until we have a key that isn't in the chains
#         # (which would mean it was the end of our original text).

#         # Note that for long texts (like a full book), this might mean
#         # it would run for a very long time.

#         word = choice(chains[key])
#         words.append(word)
#         key = (key[1], word)

#     return ' '.join(words)


# # Get the filenames from the user through a command line prompt, ex:
# # python markov.py green-eggs.txt shakespeare.txt
# filenames = sys.argv[1:]

# # Open the files and turn them into one long string
# text = open_and_read_file(filenames)

# # Get a Markov chain
# chains = make_chains(text)

# print(chains)

import random
import sys

file_name = sys.argv[1]

def open_and_read_file(file_path):
    """Take file path as string; return text as string.
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(file_name)
    text = file.read()
    return text



def make_chains(file_name):
    """Take input text as string; return dictionary of Markov chains.
    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
    For example:
        >>> chains = make_chains('hi there mary hi there juanita')
    Each bigram (except the last) will be a key in chains:
        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]
    Each item in chains is a list of all possible following words:
        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        >>> chains[('there','juanita')]
        [None]
        
        {Would, you} : [could, could, could, like, like]
    """
    full_text = open_and_read_file(file_name)
    full_text_lst = full_text.replace('(', ' ').replace(')', ' ').replace('"', ' ').rstrip().split()
    
    chains = {}

    for i in range(len(full_text_lst) - 2):
        # the next 3 lines will create a empty list and then appends the word at i(would) & i+1(you)
        key_list = []
        key_list.append(full_text_lst[i])
        key_list.append(full_text_lst[i + 1])

        key_tuple = tuple(key_list) #takes the key_list and convers it to a tuple {would, you}

        
        if key_tuple in chains.keys():
            chains.get(key_tuple).append(full_text_lst[i + 2])
        else:
            chains[key_tuple] = [full_text_lst[i + 2]]
            

    return chains


def make_text(chains):
    """Return text from chains."""

    #Set variable words to empty list to store Markov chain of text
    words = []

    #Set variable chains to dict called from make_chains function
    chains = make_chains(input_text)

    #Set variable keys to keys in dict
    keys = chains.keys()

    #Set variable first_key to a random tuple from keys
    first_key = random.choice(list(keys))

    #First word of next tuple is the second item in the first_key tuple
    first_word = first_key[1]

    #First next word is a random word from the list of values stored at
    #first_key in dict
    first_next = random.choice(list(chains[first_key]))

    #Add first item in first_key to words capitalized
    words.append(first_key[0].capitalize())

    #Add second item in first_key to words
    words.append(first_key[1])

    #Add first next word to words
    words.append(first_next)

    #Create a condition that is always true
    while len(words) < 60:

        #List of the current key
        #Item at index 0 is the second to last word in list
        #Item at index 1 is the last word in list
        current_key_list = []
        current_key_list.append(words[-2])
        current_key_list.append(words[-1])

        #Create a tuple from the list of current key
        current_key = tuple(current_key_list)

        #If current_key not in keys, break the loop
        if current_key not in keys:
            break

        #If current_key in keys, continue adding to list of words
        else:

            #Choose a random word from the list of words stored
            #as the value for the current key
            current_next = random.choice(list(chains[current_key]))

            #Add new random word to list of words
            words.append(current_next)

    #Return joined list of words
    return " ".join(words)


# # Open the file and turn it into one long string
input_text = open_and_read_file(file_name)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)