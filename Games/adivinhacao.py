import random

def jogar():

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("  SEJA BEM-VINDO AO JOGO")
    print("   Jogo da adivinhação")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

    numero_secreto = random.randrange(1,101)
    pontos = 1000
    total_tentativas = 0

    print("ESCOLHA O NÍVEL DO JOGO")
    print("Fácil   (1) - O jogador recebe 20 tentativas;")
    print("Médio   (2) - O jogador recebe 15 tentativas;")
    print("Difícil (3) - O jogador recebe 10 tentativas.")

    niveis = ["", "Fácil", "Médio", "Difícil"]
    dificuldade = niveis[int(input("\nDefine o nível: "))]

    if (dificuldade == "Fácil"):
        total_tentativas = 20
    elif (dificuldade == "Médio"):
        total_tentativas = 15
    elif (dificuldade == "Difícil"):
        total_tentativas = 10
    else:
        print("Nível selecionado inválido! Reinicie o jogo.")
        exit()

    print(f"\nNível selecionado: {dificuldade}\n")

    for rodada in range(1, total_tentativas + 1):
        print(f"Rodada {rodada} de {total_tentativas}." )
        chute = int(input("Digite um número entre 1 e 100: "))

        if (chute < 1 or chute > 100):
            print("Número inválido. Escolha um número entre 1 e 100!")
            continue

        if (chute > numero_secreto):
            print("\nO número escolhido é MAIOR que o número secreto!\n")
        elif (chute < numero_secreto):
            print("\nO número escolhido é MENOR que o número secreto!\n")
        
        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos

        if (rodada == total_tentativas):
            print("\nAcabou as suas tentativas.\nFim de jogo!")
            print(f"O número secreto era {numero_secreto}")
            break

        if (chute == numero_secreto):
            print("\nWoow. Você acertou o número secreto!")
            print(f"O número secreto é {numero_secreto}.")
            print(f"E a sua pontuação foi {pontos}.\n")
            break

if (__name__ == "__main__"):
    jogar() 