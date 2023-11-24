'''
Simulation of VIGENERE CIPHER in Python
Sample Input
Plaintext : Hello World
Key : iamnotagooduser
--> Output CipherText : Pexyc Poxzr
--> Output DecrytedText : Hello World

Note : This Code considers spaces and is caseSensitive thereby increasing the efficiency of the algorithm and Message passing. 
'''

import time

def _pad_key(plaintext, key):
    padded_key = ''
    i = 0
    for char in plaintext:
        if char.isalpha():
            padded_key += key[i % len(key)]
            i += 1
        else:
            padded_key += ' '
    return padded_key


def _encrypt_decrypt_char(plaintext_char, key_char, mode='encrypt'):
    if plaintext_char.isalpha():
        first_letter = 'a'
        if plaintext_char.isupper():
            first_letter = 'A'

        old_pos = ord(plaintext_char) - ord(first_letter)
        key_pos = ord(key_char.lower()) - ord('a')

        if mode == 'encrypt':
            new_pos = (old_pos + key_pos) % 26
        else:
            new_pos = (old_pos - key_pos + 26) % 26
        return chr(new_pos + ord(first_letter))
    return plaintext_char

def encrypt(plaintext, key):
    ciphertext = ''
    padded_key = _pad_key(plaintext, key)
    for plaintext_char, key_char in zip(plaintext, padded_key):
        ciphertext += _encrypt_decrypt_char(plaintext_char, key_char)
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    padded_key = _pad_key(ciphertext, key)
    for ciphertext_char, key_char in zip(ciphertext, padded_key):
        plaintext += _encrypt_decrypt_char(ciphertext_char, key_char, mode='decrypt')
    return plaintext

plaintext = input('Enter a message: ')
key = input('Enter a key: ')

ciphertext = encrypt(plaintext, key)
decrypted_plaintext = decrypt(ciphertext, key)


print("Encrypting...")
time.sleep(1)
print(f'Ciphertext: {ciphertext}')
time.sleep(1)
print("Decrypting... Wait a Moment...")
time.sleep(1)
print("Almost There...")
time.sleep(1)
print(f'Decrypted Plaintext: {decrypted_plaintext}')