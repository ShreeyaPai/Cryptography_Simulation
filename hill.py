import numpy as np


def encode(char):
    return ord(char)-65


def decode(num):
    return chr(num+65)


def encrypt(key, pt_arr):
    cipher_text = []
    for i in range(0, len(pt_arr), 2):
        present_term = np.zeros((2, 1))
        present_term[0][0] = pt_arr[i]
        present_term[1][0] = pt_arr[i+1]
        # print(present_term)
        present_term = np.matmul(key, present_term)
        # print(present_term)
        cipher_text.append(present_term[0][0])
        cipher_text.append(present_term[1][0])
    return cipher_text


def prep_key(k, k_s):
    key = np.zeros((k_s, k_s))
    for i in range(k_s):
        for j in range(k_s):
            key[i][j] = encode(k[i*k_s+j])
    return key


n = int(input("Welcome to the Hill Encryption.\nEnter\n1.Encryption\n2.Decryption\n"))
k_s = int(input("Enter the order of key : "))
k = input("Enter the key \n")


key = prep_key(k, k_s)
print(key)

if (n == 1):
    # print(chr(27) + "[2J")
    print("\t\t\tENCRYPTION....")
    plain_text = input("Enter the message to be Encrypted\n")
    plain_text = plain_text.upper()
    if (len(plain_text) % 2 != 0):
        plain_text = plain_text+'X'
    pt_arr = []
    for i in range(len(plain_text)):
        pt_arr.append(encode(plain_text[i]))
    cipher_arr = encrypt(key, pt_arr)

    cipher_arr = np.array(cipher_arr, dtype=int) % 26
    cipher_text_arr = []
    for i in range(len(cipher_arr)):
        cipher_text_arr.append(decode(cipher_arr[i]))
    cipher_text = ""
    cipher_text = cipher_text.join(cipher_text_arr)
    print(cipher_text)
