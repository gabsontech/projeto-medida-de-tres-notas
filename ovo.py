# def cadentrar(nomeusua,senhausua,dicausua):
#     print("dica:",dicausua,"\n"):
#     egg = int(input("entrar(1) \n sair(2) "))
#     if egg == 1:
#         entrar(nomeusua,senhausua,dicausua):
#     print("dica:",dicausua,"\n")        
#     if egg == 2:
#         cadastrar()

# def cadastrar(nomeusua,senhausua,dicausua):
#     nomeusua = str(input("nome de usuario novo: "))
#     senhausua = str(input("senha de usuario novo: "))
#     dicausua = str(input("dica de usuario novo: "))
#     return nomeusua,senhausua,dicausua
#     cadentrar()

# def entrar(nomeusua,senhausua,dicausua):
#     print("dica:",dicausua,"\n")
#     nome = str(input("nome?"))
#     senha = str(input("senha?"))

#     cadentrar(nome,senha,dicausua)
#     print("dica:",dicausua,"\n")

LISTA = []


def cadastrar():   
    nomeusua = str(input("nome de usuario novo: "))
    senhausua = str(input("senha de usuario novo: "))
    # dicausua = str(input("dica de usuario novo: "))
    cad = (nomeusua,senhausua)
    LISTA.append(cad)
    print("linha hipotetica pra entrar numa funcao de logar")

  
def entrar():  
    Nome = str(input("Nome: "))
    Senha = str(input("Senha: "))

    
    for nome,senha in LISTA:
        print(nome," ", senha)
        if nome ==  Nome and senha == Senha:
            print("Ola cara inteligente")
        else:
            print("Ola boboca")





while True:
    escolha = int(input("1 cadastrar \n 2 entrar \n 0 sair"))
    match escolha:
     case 0:
      break 
     case 1:
      cadastrar()
     case 2:
      entrar()
     case _:
      print("e 0,1 ou 2")
