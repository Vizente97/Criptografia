import fileinput
import math
from operator import xor

def main():
    for line in fileinput.input():
        if fileinput.isfirstline():
            key = line[:-1]
        plain_text = line.replace("\r","")
        plain_text = plain_text.replace("\n","")
        plain_text = plain_text.replace("\t","")
    
    array(key,plain_text)
    
def array(key,plain_text):
    S = []
    T = []
    ASCII = []
    ASCII2 = []
    j = 0

    for i in range (0, 256, 1):
        S.append(i)

    for i in key:
        temp_ASCII = ord(i)
        ASCII.append(temp_ASCII)
    
    for i in range (0, 256, 1):
        T.append(ASCII[j])
        j += 1
        if j == len(ASCII):
            j = 0
    
    j = 0
    for i in range (256):
        j = (j + S[i] + T[i]) % 256
        temp_ = S[i]
        S[i] = S[j]
        S[j] = temp_

    KeyStream = []
    j = 0
    for i in range(1,len(plain_text)+2):
        j = ((j + S[i]) % 256)
        temp_ = S[i]
        S[i] = S[j]
        S[j] = temp_
        t = (S[i] + S[j]) % 256
        KeyStream.append(S[t])
    
    for i in plain_text:
        temp_ASCII = ord(i)
        ASCII2.append(temp_ASCII)
    
    mensaje = ""
    for i in range (len(plain_text)):
        if len(hex(xor(KeyStream[i],ord(plain_text[i])))) == 3:
            mensaje += "0"
            mensaje += hex(xor(KeyStream[i],ord(plain_text[i]))).upper().split('X')[-1]
        else:
            mensaje += hex(xor(KeyStream[i],ord(plain_text[i]))).upper().split('X')[-1]

    print(mensaje)

main()