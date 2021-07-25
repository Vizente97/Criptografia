import fileinput
input_program = []
Mednm= []

def get_input():
    global input_program
    for line in fileinput.input():
        line = line.replace("\n", "")
        input_program.append(line)
        
def get_values():
    global Mednm
    global input_program
    M = (int(input_program[1])*int(input_program[2]))-1
    Mednm.append(M)
    e = (int(input_program[3])*M)+int(input_program[1])
    Mednm.append(e)
    d = (int(input_program[4])*M)+int(input_program[2])
    Mednm.append(d)
    n = ((e*d)-1)/M
    Mednm.append(n)
    m = (int(input_program[5]))%n
    Mednm.append(m)

def encryp():
    global Mednm
    x = Mednm[4]*Mednm[1]
    y = x % Mednm[3]
    print("{:.0f}".format(y))


def decryp():
    global Mednm
    y = Mednm[4]*Mednm[2]
    x = y % Mednm[3]
    print("{:.0f}".format(x))


if __name__ == "__main__":
    get_input()
    get_values()
    if input_program[0] == "E":
        encryp()
    elif input_program[0] == "D":
        decryp()
    else:
        print("Error en formato de prueba")