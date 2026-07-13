matriz = [
    ['▢','▢','▢',],
    ['▢','▢','▢',],
    ['▢','▢','▢',]
]

def imprimir_jogo():
    print('  0 1 2')
    for i in range(0,3):
        print(i, end = " ")
        for j in range(0,3):
            print(matriz[i][j], end = ' ')
        print()

def muda_matriz():
    linha = int(input("que linha tu quer mudar? 0-2"))
    coluna = int(input("qual coluna?"))
    resposta = str(input("Xis ou bolinha?"))
    matriz[linha][coluna] = resposta


imprimir_jogo()
while True:
    muda_matriz()
    imprimir_jogo()
