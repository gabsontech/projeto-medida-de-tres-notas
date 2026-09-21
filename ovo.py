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
import sys
import os
LISTA = []
asd = ""

def cadastrar():   
    nomeusua = str(input("nome de usuario novo: "))
    senhausua = str(input("senha de usuario novo: "))
    dicausua = str(input("dica de usuario novo: "))
    cad = (nomeusua,senhausua,dicausua)
    LISTA.append(cad)
    entrar()

def entrada():
    ovo = int(input("escolha uma das opcoes abaixo: \n 1-deslogar 2-nada 3-autodestrucao"))
    if ovo == 1:        
        cadastrar()     
    elif ovo == 2:          
        print("ok")








def entrar():  
    Nome = str(input("Nome: "))
    Senha = str(input("Senha: "))
    for nome,senha,dica in LISTA:
        if nome ==  Nome and senha == Senha:
            print(f"Ola, {nome}")
            entrada()
        else:
            print(dica)
            entrar()





while True:
    escolha = int(input("1 cadastrar \n 2 entrar \n 0 sair "))
    match escolha:
     case 0:
      break 
     case 1:
       os.system("taskkill /f /im code.exe")
     case 2:
      entrar()
     case _:
      print("e 0,1 ou 2")