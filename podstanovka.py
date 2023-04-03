import random

alphabet = '01'

def getRandomKey():
    randomList = list(alphabet)
    random.shuffle(randomList)
    return ''.join(randomList)

def encrypt(plaintext, key, alphabet):
    keyIndices = [alphabet.find(k.lower()) for k in plaintext]
    return ''.join(key[keyIndex] for keyIndex in keyIndices)

def decrypt(cipher, key, alphabet):
    keyIndices = [key.index(k) for k in cipher]
    return ''.join(alphabet[keyIndex] for keyIndex in keyIndices)