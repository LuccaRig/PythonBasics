Pessoas = list()
soma1 = 0
soma2 = 0
for i in range(5):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    Ncalcado= int(input('Numero Calcado: '))

    soma1 = soma1 + idade
    soma2 = soma2 + Ncalcado
    
    Pessoas.append([nome, idade, Ncalcado])


mediaI = soma1 / 5
Cmedio = soma2 / 5

Pessoas.sort()
print(Pessoas)
print(mediaI)
print(Cmedio)


