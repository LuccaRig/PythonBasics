from random import randint

def ComputerDecision():
    return randint(0, 2)

def PlayerDecision():
    while True:
        n = int(input('Selecione sua jogada: 0 = Pedra, 1 = Papel, 2 = Tesoura: \n'))
        if((n > 2) or (n < 0)):
            print('Jogada Inválida, tente novamente!')
        else: return n

def Result(ComputerDecision, PlayerDecision):
    match(PlayerDecision):
        case 0: print('Voce jogou Pedra!')
        case 1: print('Voce jogou Papel!')
        case 2: print('Voce jogou Tesoura!') 
    
    match(ComputerDecision):
        case 0: print('O computador jogou Pedra!')
        case 1: print('O computador jogou Papel!')
        case 2: print('O computador jogou Tesoura!') 
    
    if(ComputerDecision == PlayerDecision):
        print('Empate')
    elif((ComputerDecision == 0) and PlayerDecision == 1):
        print('Vitoria do jogador!')
    elif(ComputerDecision == 1 and PlayerDecision == 2):
        print('Vitoria do jogador!')
    elif(ComputerDecision == 2 and PlayerDecision == 0):
        print('Vitoria do jogador!')
    else:
        print('Você perdeu, infelizmente ;-;')



Result(ComputerDecision(), PlayerDecision())