import string
import random

xor_key = random.choice(string.printable)
print(xor_key)
print(ord(xor_key))


def encrypt(text, key):
    encrypted = []
    # to_encrypt = text.split()
    for word in text:
        for letter in list(word):
            encrypted_char = chr(ord(letter) ^ ord(key))
            mutated_char = encrypted_char.encode('utf8').decode('utf8')
            encrypted.append(mutated_char)
    return ''.join(encrypted)


def decrypt(text, key):
    decrypted = []
    for item in text:
        mutated_char = item.encode('utf8').decode('utf8')
        decrypt_char = chr(ord(mutated_char) ^ ord(key))
        decrypted.append(decrypt_char)
    return ''.join(decrypted)


message = """this is the message
with a new line"""

encrypted_message = encrypt(message, xor_key)
print(encrypted_message)
print(decrypt(encrypted_message, xor_key))
