from itertools import cycle

alphabet = '01'

def encode_vijn(text, keytext):
    f = lambda arg: alphabet[(alphabet.find(arg[0])+alphabet.find(arg[1])%2)%2]
    return ''.join(map(f, zip(text, cycle(keytext))))


def decode_vijn(coded_text, keytext):
    f = lambda arg: alphabet[alphabet.find(arg[0])-alphabet.find(arg[1])%2]
    return ''.join(map(f, zip(coded_text, cycle(keytext))))
