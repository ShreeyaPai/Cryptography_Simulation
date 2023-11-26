import random
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_keypair():
    p = q = 0
    while not is_prime(p):
        p = random.randint(50, 100)
    while not is_prime(q) or q == p:
        q = random.randint(50, 100)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = pow(e, -1, phi)

    return ((n, e), (n, d))

def encrypt(message, public_key):
    n, e = public_key
    cipher_text = [pow(ord(char), e, n) for char in message]
    return cipher_text

def decrypt(cipher_text, private_key):
    n, d = private_key
    decrypted_text = ''.join([chr(pow(char, d, n)) for char in cipher_text])
    return decrypted_text

def main():
    print("RSA Encryption and Decryption")

    # Generate key pair
    public_key, private_key = generate_keypair()
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    # Get message from the user
    message = input("Enter a message to encrypt: ")

    # Encrypt the message
    cipher_text = encrypt(message, public_key)
    print(f"Cipher Text: {cipher_text}")

    # Decrypt the message
    decrypted_text = decrypt(cipher_text, private_key)
    print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
