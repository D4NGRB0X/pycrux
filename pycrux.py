import string
import random

xor_key = random.choice([item for item in string.printable if item != ' '])
print(xor_key)
print(ord(xor_key))

if ord(xor_key) != 32:
    def encrypt(text, key):
        encrypted = []
        # to_encrypt = text.split()
        for word in text:
            encrypted_char = chr(ord(word) ^ ord(key))
            # mutated_char = encrypted_char.decode('utf8')
            encrypted.append(encrypted_char)
        return ''.join(encrypted)


    def decrypt(text, key):
        decrypted = []
        for item in text:
            # mutated_char = item.encode('utf8').decode('utf8')
            decrypt_char = chr(ord(item) ^ ord(key))
            decrypted.append(decrypt_char)
        return ''.join(decrypted)
else:
    print("rerun")

message = """this is the message
with a new line"""

encrypted_message = encrypt(message, xor_key)
print(encrypted_message)
print(decrypt(encrypted_message, xor_key))
