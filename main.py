from gammirovanie import encode_vijn, decode_vijn
from podstanovka import getRandomKey, encrypt, decrypt
from perexod import encode, decode

alphabet = '01'

def main():
    #filename = input("Введите название файла(с расширением): ")
    filename = "text.txt"
    file1 = []
    with open(filename, 'rb') as f:
        content = list(f.read())

    for i in range(len(content)):
        X = str(bin(content[i]))
        if len(X) < 9:
            while len(X) < 9:
                    X = (X[:2]) + "0" + (X[2:])
        file1.append(X)

    encrypt_file(filename, file1)
    decrypt_file(filename)



def encrypt_file(filename, file_hex):
    key1 = getRandomKey() #подстановка ключ
    key2 = int(len(file_hex) / 2) #перестановка ключ
    key3 = '1111' #гаммирование ключ

    plaintext = file_hex
    cipher11 = []
    for x in range(len(plaintext)):
        cipher11.append(plaintext[x][2:])

    cipher_main = []
    print("0: ", plaintext)
    for i in range(len(cipher11)):
        cipher1 = encrypt(cipher11[i], key1, alphabet)
        cipher2 = encode(cipher1, key2)
        cipher3 = encode_vijn(cipher2, key3)
        #print("1 ", cipher1, " 2 ", cipher2, " 3 ", cipher3 )
        cipher_main.append(str(plaintext[i][:2] + cipher3))
    print("main ", cipher_main, '\n')

    my_file = open("key.txt", "w+")
    my_file.write(str(key1)+'\n'+str(key2)+'\n'+str(key3))
    my_file.close()

    filename1 = 'encrypt_' + filename
    my_file = open(filename1, "wb+")
    for q in range(len(cipher_main)):
        X = bytes(str(int(cipher_main[q], 2)), 'utf-8')
        print(X)
        #write = X.to_bytes((X.bit_length() + 7) // 8, 'big').decode()
        #my_file.write(str(write))
        my_file.write(X)
    my_file.close()


def decrypt_file(file):
    filename2 = 'encrypt_' + file
    file2 = []

    with open(filename2, 'rb') as f:
        content:str = list(f.read())


    for i in range(len(content)):
        X = str(bin(content[i]))
        if len(X) != 9:
            while len(X) < 9:
                    X = (X[:2]) + "0" + (X[2:])
        file2.append(X)


    key = ['','','']
    with open("key.txt", "r") as f:
        pere = 0
        for line in f.readlines():
            key[pere] = line
            pere += 1

    decipher11 = []
    for x in range(len(file2)):
        decipher11.append(file2[x][2:])

    decipher_main = []
    print("10: ", file2)
    for i in range(len(decipher11)):
        decrypt3 = decode_vijn(decipher11[i], key[2])
        decrypt2 = decode(decrypt3,int(key[1]))
        decrypt1 = decrypt(decrypt2, key[0], alphabet)
        #print("10 ", decrypt3, " 20 ", decrypt2, " 30 ", decrypt1 )
        decipher_main.append(str(file2[i][:2] + decrypt1))
    print("main ", decipher_main, '\n')



    filename3 = 'decrypt_' + file
    my_file = open(filename3, "w+")
    for q in range(len(decipher_main)):
        write_N = int(decipher_main[q], 2)
        write = write_N.to_bytes((write_N.bit_length() + 7) // 8, 'big').decode()
        my_file.write(write)
        print(write)
    my_file.close()

if __name__ == "__main__":
    main()