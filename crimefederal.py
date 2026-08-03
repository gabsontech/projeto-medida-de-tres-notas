matriz = [
    ['▢','▢','▢',],
    ['▢','▢','▢',],
    ['▢','▢','▢',]
]
def istdiebesten():
    print("parabens!! acabou!!! é campeao!!!")
    
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
#
    if matriz[2][2] and matriz[1][1] and matriz[0][0] == "X":
        istdiebesten()
    if matriz[0][2] and matriz[1][2] and matriz[2][2] == "X":
        istdiebesten()
    if matriz[0][1] and matriz[1][1] and matriz[2][1] == "X":
        istdiebesten()
    if matriz[0][0] and matriz[1][0] and matriz[2][0] == "X":
        istdiebesten()
    if matriz[1][0] and matriz[1][1] and matriz[1][2] == "X":
        istdiebesten()
    if matriz[2][0] and matriz[2][1] and matriz[2][2] == "X":
        istdiebesten()
    if matriz[0][2] and matriz[1][1] and matriz[2][0] == "X":
        istdiebesten()
    if matriz[2][2] and matriz[1][1] and matriz[0][0] == "O":
        istdiebesten()
    if matriz[0][2] and matriz[1][2] and matriz[2][2] == "O":
        istdiebesten()
    if matriz[0][1] and matriz[1][1] and matriz[2][1] == "O":
        istdiebesten()
    if matriz[0][0] and matriz[1][0] and matriz[2][0] == "O":
        istdiebesten()
    if matriz[1][0] and matriz[1][1] and matriz[1][2] == "O":
        istdiebesten()
    if matriz[2][0] and matriz[2][1] and matriz[2][2] == "O":
        istdiebesten()
    if matriz[0][2] and matriz[1][1] and matriz[2][0] == "O":
        istdiebesten()
   #
    if resposta == "X" or resposta == "O":
        matriz[linha][coluna] = resposta
    else:
        print("e so X ou O maiusculo")
        muda_matriz()


imprimir_jogo()
while True:
    muda_matriz()
    imprimir_jogo()
