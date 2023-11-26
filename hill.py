import numpy as np


def encode(char):
    return ord(char)-65


def decode(num):
    return chr(num+65)


def en_de_crypt(key, pt_arr, k_s):
    cipher_text = []
    if k_s == 2:
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
    if k_s == 3:
        for i in range(0, len(pt_arr), 3):
            present_term = np.zeros((3, 1))
            present_term[0][0] = pt_arr[i]
            present_term[1][0] = pt_arr[i+1]
            present_term[2][0] = pt_arr[i+2]
            # print(present_term)
            present_term = np.matmul(key, present_term)
            # print(present_term)
            cipher_text.append(present_term[0][0])
            cipher_text.append(present_term[1][0])
            cipher_text.append(present_term[2][0])
        return cipher_text


def prep_key(k, k_s):
    key = np.zeros((k_s, k_s))
    for i in range(k_s):
        for j in range(k_s):
            key[i][j] = encode(k[i*k_s+j])
    return key


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("The multiplicative inverse does not exist.")
    else:
        return (x % m + m) % m


def matrix_adjoint(matrix):
    # Calculate the cofactor matrix
    cofactor_matrix = np.zeros_like(matrix, dtype=int)
    rows, cols = matrix.shape

    for i in range(rows):
        for j in range(cols):
            minor_matrix = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            cofactor = ((-1) ** (i + j)) * \
                int(round(np.linalg.det(minor_matrix)))
            cofactor_matrix[i, j] = cofactor

    # Transpose the cofactor matrix to get the adjoint
    adjoint_matrix = cofactor_matrix.T

    return adjoint_matrix


def key_inv(key):
    det = np.linalg.det(key)
    det = det % 26
    inv = mod_inverse(int(det), 26)
    return np.round(inv)


n = int(input("Welcome to the Hill Encryption.\nEnter\n1.Encryption\n2.Decryption\n"))
k_s = int(input("Enter the order of key : (Ex. Enter 3 for 3*3 matrix)\n"))
k = input("Enter the key \n")
key = prep_key(k, k_s)

if (n == 1):
    print(chr(27) + "[2J")
    print("\t\t\tENCRYPTION....")
    plain_text = input("Enter the message to be Encrypted\n")
    plain_text = plain_text.upper()
    if (len(plain_text) % 2 != 0):
        plain_text = plain_text+'X'
    pt_arr = []
    for i in range(len(plain_text)):
        pt_arr.append(encode(plain_text[i]))
    cipher_arr = en_de_crypt(key, pt_arr, k_s)

    cipher_arr = np.array(cipher_arr, dtype=int) % 26
    cipher_text_arr = []
    for i in range(len(cipher_arr)):
        cipher_text_arr.append(decode(cipher_arr[i]))
    cipher_text = ""
    cipher_text = cipher_text.join(cipher_text_arr)
    print("Encoded Cipher Text is : \n")
    print(cipher_text)


if n == 2:
    print(chr(27) + "[2J")
    cipher_arr = en_de_crypt(key, pt_arr, k_s)
    det_inv = key_inv(key)
    adj = matrix_adjoint(key) % 26
    inv = (det_inv * adj) % 26
    print("\t\t\tDECRYPTION...")
    cipher_text = input("Enter the message to be Decrypted\n")
    cipher_text = cipher_text.upper()
    if (len(cipher_text) % 2 != 0):
        cipher_text = cipher_text+'X'

    ct_arr = []
    for i in range(len(cipher_text)):
        ct_arr.append(encode(cipher_text[i]))
    pt_arr = en_de_crypt(inv, ct_arr, k_s)  # decrypt

    pt_arr = np.array(pt_arr, dtype=int) % 26
    pt_text_arr = []
    for i in range(len(pt_arr)):
        pt_text_arr.append(decode(pt_arr[i]))
    plain_text = ""
    plain_text = plain_text.join(pt_text_arr)
    print("Decoded Plain Text is : \n")
    print(plain_text)
