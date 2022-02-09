#adivinhação.py
import random

def jogar():
    print(" ******************************** ")
    print(" Bem vindo ao Jogo de Adivinhação ")
    print(" ******************************** ")



    numero_secreto = random.randrange(1,5)
    total_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil - 20 tentativas")
    print("(2) Médio - 10 tentativas")
    print("(3) Difícil - 5 tentativas")

    nível = int(input("Define o nível: "))

    if (nível == 1):
        total_tentativas = 20
    elif (nível == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5
            

    for tentativa in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(tentativa, total_tentativas))
        jogador = int(input("Digite um número: "))
        
        if (jogador == numero_secreto):
            print (" Parabéns você acertou ")
            break
        else:
            pontos_perdidos = abs(numero_secreto - jogador)
            pontos = pontos - pontos_perdidos
            
            if (jogador > numero_secreto):
                print (" Errou, o numero era menor".format(numero_secreto))
            else:
                print (" Errou, o numero era maior".format(numero_secreto))

    print('**Fim de jogo**')
    print(f'O número secreto era {numero_secreto}. Você fez {pontos} pontos.')

if (__name__=="__main__"):
    jogar()
        
       
    
