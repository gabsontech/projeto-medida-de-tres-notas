print("eae, duvida que eu adivinhe tua idade exata?")
anoatual = int(input("qual é o ano atual? "))
anonasc = int(input("qual é o ano de nascimento? "))
mesatual = int(input("qual é o mês atual? "))
mesnasc = int(input("qual é o mês de nascimento? "))
diaatual = int(input("qual é o dia atual? "))
dianasc = int(input("qual é o dia de nascimento? "))
if mesnasc > mesatual: 
    idade = anoatual - anonasc - 1
if not mesnasc > mesatual and dianasc > diaatual and mesnasc == mesatual and dianasc == diaatual:
    idade = anoatual - anonasc
if mesnasc > mesatual:
    idade = anoatual - anonasc - 1
if mesatual < mesnasc and diaatual > dianasc:
    idade = anoatual - anonasc - 1
if mesatual == mesnasc and diaatual == dianasc:
    idade = anoatual - anonasc
print("voce tem",idade)