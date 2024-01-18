# Text Sequence Type — str
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
from random import *

def jogar():

    # Abre o arquivo e cria uma lista usando as palavras salvas
    arquivo = open("forca_palavras.txt")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    # Gera um número aleatório para escolher a palavra secreta
    numero = randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    # Gera uma lista para apresentar ao jogador a quantidade de letras da palavra secreta
    letras_corretas = ["_" for letra in palavra_secreta]

    # Variáveis que vão definir o status do jogo
    enforcou = False
    acertou = False
    erros = 0

    print(f"Você tem {6 - erros} tentativas. Boa sorte.")
    # len() retorna a quantidade de elementos em uma lista ou a quantidade de caracteres em uma frase
    print(f"\nA palavra secreta tem {len(letras_corretas)} letras!")
    print(letras_corretas)

    # Loop infinito enquanto as condições são falsas
    while (not enforcou and not acertou):

        # strip() -> Remove os espaços da string e o \n (que usamos para pular a linha)
        # upper() -> Converte a string para letras maiúsculas
        chute = input("\nEscolha uma letra: ").strip().upper()
        
        if (chute in palavra_secreta):
            posicao = 0

            # Esse FOR percorre toda a string e separa as posições de cada letra da palavra secreta
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_corretas[posicao] = letra
                posicao += 1

            if (chute in letras_corretas):
                print(f"\nNice! Você acertou {letras_corretas.count(chute)} letra(s).")
                print("Veja como ficou a palavra secreta:")
        else:
            erros += 1
            print(f"\nOps, você errou! Faltam {6 - erros} tentativas.")

        enforcou = erros == 6
        acertou = "_" not in letras_corretas

        print(letras_corretas)
        print(f"\nQuantidade de letras ocultas: {letras_corretas.count("_")}")
        print(f"Tentativas restantes: {6 - erros}")
    
    if (acertou):
        print("\nParabéns, você acertou a palavra secreta!")
    else:
        print("\nQue pena, você não conseguiu descobrir a palavra secreta e foi enforcado.")

if (__name__ == "__main__"):
    jogar()