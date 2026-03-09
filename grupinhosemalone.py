alunosnasala=int(input("quantos alunos tem na tua sala?"))
ovo=int(input("quantas pessoas em cada grupo??"))
asdasd=alunosnasala // ovo
hahah = alunosnasala % ovo
if hahah == 0:
    pao = "uhul sobrou ninguém"
if not hahah == 0:
    pao = ""
print("cada grupo tem",asdasd,"pessoas ok, sobrou",hahah,pao)
