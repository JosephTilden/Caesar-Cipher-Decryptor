# DO NOT CHANGE THIS FILE!!

from caesar import *

def read_message_string(file_name):
    """
    Returns: a possibly profound message in encrypted text.
    """
    in_file = open(file_name, "r")
    message = str(in_file.read())
    in_file.close()
    return message

# Unit test - verify that create_shift_table is properly implemented.

message = "Hello, World!"
print("*** create_shift_table:", end=" ")
assert create_shift_table(-1) == None
assert create_shift_table(N_LETTERS) == None

n_errors = 0
for i in range(N_LETTERS):
    table = create_shift_table(i)
    if table == None or len(table) != N_LETTERS * 2:
        n_errors += 1
        break
    for key in table:
        alt = table[key]
        if key.isupper():
            base = ord('A')
        elif key.islower():
            base = ord('a')
        org = chr(((ord(key) - base) + i) % N_LETTERS + base)
        if alt != org:
            n_errors += 1

if n_errors == 0:
    print("PASSED")
else:
    print("FAILED")

# Unit test - verify that apply_shift is properly implemented.
print("*** apply_shift:", end=' ')
result = apply_shift(message, 1)
if result != 'Ifmmp, Xpsme!':
    print("FAILED")
else:
    print("PASSED")

# Test encryption.

print("*** encrypt_text:", end=' ')
plaintext = 'Python is pretty useful.'
expected = 'Ravjqp ku rtgvva wughwn.'
actual = encrypt_message(plaintext, 2)
if expected == actual:
    print("PASSED")
else:
    print("FAILED")
    print('  Expected Output:', expected)
    print('  Actual Output:', actual)
# Test is_word

print("*** is_word:", end=' ')
if (is_word('KNIFE!') and is_word('Dirigible') and is_word(" acrobatics ") and
    not is_word("and but or") and not is_word('xyzzy')):
    print("PASSED")
else:
    print("FAILED")

print("*** decrypt_text:", end=' ')
ciphertext = "Kdssb Vxpphu, L krsh!"
expected = (23, 'Happy Summer, I hope!')
actual = decrypt_message(ciphertext)
if expected == decrypt_message(ciphertext):
    print("PASSED")
else:
    print("FAILED")
    print('  Expected Output:', expected)
    print('  Actual Output:', actual)

# Actually try to decode the message.

ciphertext = read_message_string("message.txt")
result = decrypt_message(ciphertext)
if result != None:
    print("Best shift:", result[0])
    print(result[1])
