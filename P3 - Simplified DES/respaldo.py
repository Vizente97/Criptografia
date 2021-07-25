import fileinput
from operator import xor

def get_input():
    entrada = [] 
    i = 0
    for line in fileinput.input():
        entrada.append(line)
        entrada[i] = entrada[i].replace("\r","")
        entrada[i] = entrada[i].replace("\n","")
        entrada[i] = entrada[i].replace("\t","")
        i += 1
    option = entrada[0]
    Key = entrada[1] 
    plain_text = entrada[2]     
    return option, Key, plain_text

def subkey(key):
    temp = [] 
    subkey_temp = [] 
    for i in key:
        temp.append(int(i))
    perm = [2,4,1,6,3,9,0,8,7,5]
    for i in range(len(perm)):
        subkey_temp.append(key[perm[i]])
    list_1 = subkey_temp[:len(subkey_temp)//2]
    list_1 = list_1[1:5] + list_1[0:1]
    list_2 = subkey_temp[len(subkey_temp)//2:]
    list_2 = list_2[1:5] + list_2[0:1]
    subkey_1 = get_subkey(list_1+list_2)
    list_1 = list_1[2:5] + list_1[0:2]
    list_2 = list_2[2:5] + list_2[0:2]
    subkey_2 = get_subkey(list_1+list_2)
    return subkey_1, subkey_2

def get_subkey(subkey1):
    subkey = []
    #index = [5,2,6,3,7,4,9,8]
    #for i in range(len(index)):
    #    subkey.append(subkey1[index[i]])
    subkey = permutations(subkey1,[5,2,6,3,7,4,9,8])
    return subkey

#def permutation(plain_text):
#    temp = []
#    permutationFinal = []
#    for i in plain_text:
#        temp.append(int(i))
#    permutationFinal = permutations(temp,[1,5,2,0,3,7,4,6])
#    return permutationFinal

def feistel(firt_perm,subkey1):
    temp = []
    left = []
    right = []
    right0 = []
    final_right = []
    final = []
    step4 = []
    for i in firt_perm:
        temp.append(int(i))
    exp = [7,4,5,6,5,6,7,4]
    for i in range(len(exp)):
        right.append(xor(temp[exp[i]],int(subkey1[i])))
        if(i<=3):
            left.append(temp[i])
        elif(i<=7):
            right0.append(temp[i])
    right1 = right[:len(right)//2]
    right2 = right[len(right)//2:]
    S0S1 = list((matriz(right1,0))+(matriz(right2,1)))
    for i in range(len(S0S1)):
        S0S1[i] = int(S0S1[i])
    perm = [1,3,2,0]
    for i in range(len(perm)):
        final_right.append(S0S1[perm[i]])
        final.append(xor(left[i],final_right[i]))        
    final = final + right0
    return final

def switch(feistelresult):
    feistelresult = feistelresult[len(feistelresult)//2:] + feistelresult[:len(feistelresult)//2]
    return feistelresult

def permutations(lista_val,lista_perm):
    perm = []
    for i in range(len(lista_perm)):
        perm.append(lista_val[lista_perm[i]])
    return(perm)

def matriz(valores,n_S):
    S0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
    S1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
    fila = (int(str(valores[0])+str(valores[3]),2))
    columna = (int(str(valores[1])+str(valores[2]),2))
    if (n_S == 0):
        valor = S0[fila][columna]
    if (n_S == 1):
        valor = S1[fila][columna]
    valor = bin(valor)
    valor = valor.replace("0b","0")
    if len(valor) > 2:
        valor = valor[1:3]
    return valor

if __name__ == "__main__":
    option, Key, plain_text = get_input()
    subkey1, subkey2 = subkey(Key)
    if option == "E":
        #firt_perm = (permutation(plain_text))
        firt_perm = permutations(plain_text,[1,5,2,0,3,7,4,6])
        valor_feistelK1 = feistel(firt_perm,subkey1)
        resultSwitch = switch(valor_feistelK1)
        valor_feistelK2 = feistel(resultSwitch,subkey2)
        print(permutations(valor_feistelK2,[3,0,2,4,6,1,7,5]))
    elif option == "D":
        #firt_perm = (permutation(plain_text))
        firt_perm = permutations(plain_text,[1,5,2,0,3,7,4,6])
        valor_feistelK2 = feistel(firt_perm,subkey2)
        resultSwitch = switch(valor_feistelK2)
        valor_feistelK1 = feistel(resultSwitch,subkey1)
        print(permutations(valor_feistelK1,[3,0,2,4,6,1,7,5]))
    