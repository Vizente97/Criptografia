import fileinput

def decrypt(matriz,type_, phrase):
    array_one = []
    array_two = []
    msg = ""

    array_one, array_two = search(matriz,type_, phrase)
    
    #raise Exception("La longitud es: ",len(phrase))

    index = 0
    for index in range(len(array_one)):
        msg += matriz[array_one[index]][array_two[index]]
    print(msg)


def encrypt(matriz,type_, phrase):
    array_one = []
    array_two = []
    array_total = []
    msg = ""

    array_one, array_two = search(matriz,type_, phrase)
    array_total = array_one + array_two

    index = 0
    while index < len(array_total):
        msg += matriz[array_total[index]][array_total[index+1]]
        index += 2
    print(msg)

def search(matriz,type_, phrase):
    array_one = []
    array_two = []

    index = 0
    while index < len(phrase):
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if(matriz[i][j]==phrase[index]):
                    if type_ == "DECRYPT":
                        if len(array_one) < len(phrase):
                            array_one.append(i)
                            if len(array_one) < len(phrase):
                                array_one.append(j)
                            else:
                                array_two.append(j)
                        else:
                            array_two.append(i)
                            array_two.append(j)
                    elif type_ == "ENCRYPT":
                        array_one.append(i)
                        array_two.append(j)
                    
        index += 1

    return(array_one,array_two)


def main():
    matriz = [["E","N","C","R","Y"],["P", "T", "A", "B", "D"],
            ["F", "G", "H", "I", "K"],["L", "M", "O", "Q", "S"],
            ["U", "V", "W", "X", "Z"]]

    for line in fileinput.input():
        if fileinput.isfirstline():
            type_ = line[:-1]
        phrase = line.replace(" ","")
        phrase = phrase.replace("\r","")
        phrase = phrase.replace("\n","")
        phrase = phrase.replace("\t","")
    if type_ == "DECRYPT":
        decrypt(matriz,type_, phrase)
    elif type_ == "ENCRYPT":
        encrypt(matriz,type_, phrase)
    else:
        print("Error File")

main()