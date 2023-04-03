from gammirovanie import encode_vijn, decode_vijn
from podstanovka import getRandomKey, encrypt, decrypt
from perexod import encode, decode

alphabet = '01'

def encrypting(filename, content):
    X = []
    for i in range(len(content)):
        y = str(bin(content[i]))
        if len(y) != 10:
            while len(y) < 10:
                y = (y[:2]) + "0" + (y[2:])
        X.append(y)
    #print(X, " - бин ориг")

    cipher11 = []
    for x in range(len(X)):
        cipher11.append(X[x][2:])

    key1 = getRandomKey()  # подстановка ключ
    key2 = int(len(content) / 2)  # перестановка ключ
    key3 = '10101'  # гаммирование ключ

    my_file = open("key.txt", "w+")
    my_file.write(str(key1)+'\n'+str(key2)+'\n'+str(key3))
    my_file.close()
    String = ""
    cipher_main = []
    for i in range(len(cipher11)):
        cipher1 = encrypt(cipher11[i], key1, alphabet)
        cipher2 = encode(cipher1, key2)
        cipher3 = encode_vijn(cipher2, key3)
        # print("1 ", cipher1, " 2 ", cipher2, " 3 ", cipher3 )
        cipher_main.append(str("0b" + cipher3))
        String = String + str(cipher3)
    #print("main1 ", cipher_main, '\n')

    intov = []

    for q in range(len(cipher_main)):
        intov.append(int(cipher_main[q], 2))

    print(intov, " инты шифра ")
    #print(String)

    filename1 = 'encrypt_' + filename
    my_file = open(filename1, "wb+")
    my_file.write(bytearray(intov))
    my_file.close()

def decrypting(filename):
    filename2 = 'encrypt_' + filename
    with open(filename2, 'rb') as f:
        content: str = list(f.read())
    #print(content, " - откр шифра")

    X = []
    for i in range(len(content)):
        #X.append(bin(content[i]))
        y = str(bin(content[i]))
        if len(y) != 10:
            while len(y) < 10:
                y = (y[:2]) + "0" + (y[2:])
        X.append(y)
    #print(X, " - бин откр шифра")

    decipher11 = []
    for x in range(len(X)):
        decipher11.append(X[x][2:])
    #print(decipher11, " - бин без 0б")

    key = ['','','']
    with open("key.txt", "r") as f:
        pere = 0
        for line in f.readlines():
            key[pere] = line
            pere += 1

    decipher_main = []
    for i in range(len(decipher11)):
        decrypt3 = decode_vijn(decipher11[i], key[2])
        decrypt2 = decode(decrypt3,int(key[1]))
        decrypt1 = decrypt(decrypt2, key[0], alphabet)
        #print("10 ", decrypt3, " 20 ", decrypt2, " 30 ", decrypt1 )
        decipher_main.append(str("0b" + decrypt1))
    #print("main2 ", decipher_main, '\n')

    deintov = []
    for q in range(len(decipher_main)):
        deintov.append(int(decipher_main[q], 2))
    print(deintov, " инт готовый ")


    filename3 = 'decrypt_' + filename
    my_file = open(filename3, "wb+")
    my_file.write(bytearray(deintov))
    my_file.close()

def main():
    filename = input("Введите название файла(с расширением): ")
    with open(filename, 'rb') as f:
        content = list(f.read())
        print(content, " - ориг")
    encrypting(filename,content)
    decrypting(filename)

if __name__ == "__main__":
    main()

