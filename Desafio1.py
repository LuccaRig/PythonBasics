Pessoas = list()
ListCalcados = []
soma1 = 0
soma2 = 0
for i in range(5):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    Ncalcado= int(input('Numero Calcado: '))

    soma1 = soma1 + idade
    ListCalcados.append(Ncalcado)
    
    Pessoas.append([nome, idade, Ncalcado])


mediaI = soma1 / 5
Pessoas.sort()
Cmedio = ListCalcados[2]

print(Pessoas)
print(mediaI)
print(Cmedio)


