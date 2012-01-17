"""
Problem 59
Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
For unbreakable encryption, the key is the same length as the plain text message,
and the key is made up of random bytes. The user would keep the encrypted message
and the encryption key in different locations, and without both "halves",
it is impossible to decrypt the message.
Unfortunately, this method is impractical for most users, so the modified method is
to use a password as a key. If the password is shorter than the message, which is likely,
the key is repeated cyclically throughout the message. The balance for this method is using
a sufficiently long password key for security, but short enough to be memorable.
Your task has been made easy, as the encryption key consists of three lower case characters.
Using cipher1.txt (right click and 'Save Link/Target As...'), a file containing the encrypted
ASCII codes, and the knowledge that the plain text must contain common English words,
decrypt the message and find the sum of the ASCII values in the original text.
"""
from itertools import permutations

def encrypt(iterable, key):
    """
    Function to encrypt a given iterable using a key
    The key can also be an iterable or any atomic type
    """
    encrypted_data = []

    # Some type checking
    if type(key) not in (list, tuple):
        try:
            key = list(key)
        except TypeError:
            key = [key]

    # The encryption process
    for i in range(0, len(iterable), len(key)):
        try:
            for j in range(len(key)):
                encrypted_data.append(ord(iterable[i + j]) ^ key[j])
        except IndexError:
            break

    return encrypted_data

def decrypt(iterable, key):
    """
    Function to decrypt a given iterable using a key
    The key can also be an iterable or any atomic type
    """
    decrypted_data = []

    # Some type checking and conversions
    if type(key) not in (list, tuple):
        try:
            key = list(key)
        except TypeError:
            key = [key]

    # The Decryption process
    for i in range(0, len(iterable), len(key)):
        try:
            for j in range(len(key)):
                decrypted_data.append(chr(iterable[i + j] ^ key[j]))
        except IndexError:
            break

    return decrypted_data


def brute_force():
    # Getting the data from the file
    f = open("cipher1.txt").read().split(",")
    x = [int(n) for n in f]

    # Generating keys and checking
    alpha = "abcdefghijklmnopqrstuvwxyz"

    # Determined by trial and error
    max = 200
    max_key = None
    for t_key in permutations(alpha, 3):
        key = [ord(a) for a in t_key]
        data = ''.join(decrypt(x, key))

        # Applying frequency analysis for space
        if max < data.count(' '):
            max = data.count(' ')
            max_key = key
            print max, t_key, ''.join(data)

    ans = decrypt(x, max_key)
    ans = [ord(char) for char in ans]
    ans = sum(ans)

    return ans

print "Answer: ", brute_force()
