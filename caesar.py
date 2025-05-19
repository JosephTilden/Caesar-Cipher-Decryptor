"""
Joseph Tilden, 2232496
420-LCU Computer Programming , Section 2
Friday , May 03
J. Gullifer , instructor
Assignment 4
"""

#*** You will add your code to this file. ***

import string

### DO NOT MODIFY THIS FUNCTION ###
def read_word_list(file_name):
    '''
    file_name (str): the name of the file containing the list of words
    to load.
    
    Returns: a set of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    in_file = open(file_name, 'r') # in_file: file
    line = in_file.readline()      # line: str
    word_list = line.split()       # word_list: list of str
    in_file.close()
    return frozenset(word_list)    # creates an immutable set.

N_LETTERS = len(string.ascii_lowercase)
VALID_WORDS = read_word_list('words.txt')

def string_to_shift_table(letter_string, shift):
    '''
    This function takes string of letters, and makes a dictionary where the
    keys are the letters in the string and the values are those same letters
    shifted over to the right by the integer specified in the second input.
    '''
    # Make letter and position lists and zip them up in a dictionary
    letters = []
    position = 0
    pos_table = []
    for char in letter_string:
        letters.append(char)
        pos_table.append(position)
        position += 1
    letter_position_dict = dict(zip(letters, pos_table))
    # Replace the positional values with shifted letters
    for letter in letter_position_dict:
        if letter_position_dict[letter] + shift < N_LETTERS:
            letter_position_dict[letter] = letters[
                letter_position_dict[letter] + shift]
        # For wraparound case
        else:
            letter_position_dict[letter] = letters[
                letter_position_dict[letter] + shift - N_LETTERS]
    # Keys = regular letters, values = shifted letters
    return letter_position_dict

#assert shift_and_flip(string.ascii_lowercase, 3) != 2
#assert
#assert

# IMPLEMENT THIS FUNCTION
def create_shift_table(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.        
        
    shift (int): the amount by which to shift every letter of the 
    alphabet, 0 <= shift < N_LETTERS. If shift is less than zero or
    greater than or equal to N_LETTERS, this function should return
    None.

    Returns: a dictionary mapping a letter (str) to another
             letter (str), for all lower and upper case letters.
    '''
    # YOUR CODE HERE
    if 0 <= shift < N_LETTERS:
        # Encrypt lowercase letters
        lowercase_letters = string.ascii_lowercase
        lowercase_table = string_to_shift_table(lowercase_letters, shift)
        # Do the same for uppercase letters
        uppercase_letters = string.ascii_uppercase
        uppercase_table = string_to_shift_table(uppercase_letters, shift)
        # Use .update() to put the two dictionaries together. I found this
        # method online. 
        all_case_table = lowercase_table.copy()
        all_case_table.update(uppercase_table)
        return all_case_table
    else:
        return None

#x = create_shift_table(3)
assert create_shift_table(3) != None

### IMPLEMENT THIS FUNCTION
def apply_shift(original_text, shift):
    '''
    Applies the Caesar Cipher to original_text with the input shift.
    Creates a new string that is original_text shifted down the
    alphabet by some number of characters determined by the input shift        
    shift (int): the shift with which to encrypt the message.
    0 <= shift < N_LETTERS

    Returns: the message text (str) in which every character is shifted
             down the alphabet by the input shift
    '''
    # YOUR CODE HERE
    reference_table = create_shift_table(shift)
    shifted_text = ""    # To hold altered text
    # Shift each character in original_text and add them to a new string
    for char_pos in range(len(original_text)):
        char = original_text[char_pos]
        if char.isalpha():
            shifted_text += reference_table[char]
        # If char is not a letter then just add it without changing
        else:
            shifted_text += char
    return shifted_text

### IMPLEMENT THIS FUNCTION
def encrypt_message(original_text, shift):
    '''
    Used to encrypt the message using the given shift value.
        
    Returns: The encrypted string.
    '''
    # YOUR CODE HERE
    return apply_shift(original_text, shift)

### IMPLEMENT THIS FUNCTION
def is_word(word):
    '''
    Determines if word is a valid word, ignoring
    capitalization, punctuation, and possible spaces.
        
    word (str): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word('Bat')
    True
    >>> is_word('asdf')
    False
    '''
    # YOUR CODE HERE
    cleaned_word = word.strip(string.whitespace).strip(string.punctuation
                                                       ).lower()
    if cleaned_word in VALID_WORDS:
        return True
    else:
        return False

### IMPLEMENT THIS FUNCTION ###
def decrypt_message(cipher_text):
    '''
    Decrypt cipher_text by trying every possible shift value
    and find the "best" one. We will define "best" as the shift that
    creates the maximum number of real words when we use apply_shift(shift)
    on the text. If s is the original shift value used to encrypt
    the message, then we would expect N_LETTERS - s to be the best shift value 
    for decrypting it.

    Note: if multiple shifts are equally good such that they all create 
    the maximum number of words, you may choose any of those shifts (and 
    their corresponding decrypted messages) to return

    Returns: a tuple of the best shift value used to decrypt the message
    and the decrypted message text using that shift value.
    '''
    # YOUR CODE HERE
    shift_tests_dict = {}    # To hold shifts and their valid word counts
    best_shift = 0           # Will be changed if another shift is better
    word_list = cipher_text.split()    # Break text up into words
    # Test for all possible shifts
    for shift in range(N_LETTERS):
        valid_words = 0        
        # Check for valid words
        for word in word_list:
            if is_word(encrypt_message(word, shift)):
                valid_words += 1
        # Add shift and its valid words to the dictionary
        shift_tests_dict[shift] = valid_words
    # Found how to get the key with the highest value online
    best_shift = max(shift_tests_dict, key=shift_tests_dict.get)
    return (best_shift, encrypt_message(cipher_text, best_shift))

