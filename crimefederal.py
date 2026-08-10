matriz = [
    ['▢','▢','▢',],
    ['▢','▢','▢',],
    ['▢','▢','▢',]
]
def ovo():
    print("acabou!!ashdbhabsdabdjbsdbads")
def imprimir_jogo():
    print('  0 1 2')
    for i in range(0,3):
        print(i, end = " ")
        for j in range(0,3):
            print(matriz[i][j], end = ' ')
        print()

def muda_matriz():
    linha = int(input("que linha tu quer mudar? 0-2: "))
    coluna = int(input("qual coluna? 0-2: "))
    resposta = str(input("Xis ou bolinha? X-O: "))
    for i in range(0,3):
        for j in range(0,3):
            if matriz[i][j] == "X":
                "O" == False
            elif matriz[i][j] == "O":
                "X" == False
            else:
                "O" == False
                "X" == False
                if "X" == True:
                    return -1
                elif "O" == True:
                    return 1
    if resposta == "X" or resposta == "O":
        matriz[linha][coluna] = resposta
    else:
        print("e so X ou O maiusculo")
        muda_matriz()


imprimir_jogo()
while True:
    muda_matriz()
    imprimir_jogo()
