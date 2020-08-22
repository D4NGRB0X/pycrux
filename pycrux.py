import string
import random

xor_key = random.choice(string.ascii_letters)
print(xor_key)
print(ord(xor_key))


def encrypt(text, key):
    encrypted = []
    if isinstance(text, str):
        to_encrypt = text.split()
        for word in to_encrypt:
            for letter in list(word):
                encrypted_char = chr(ord(letter) ^ ord(key))
                encrypted.append(encrypted_char.encode('utf8').decode('utf8'))
    return ''.join(encrypted)
# def decrypt()


message = "this is the message"

print(encrypt(message, xor_key))
