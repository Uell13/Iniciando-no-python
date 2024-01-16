# Text Sequence Type — str
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

def jogar():

    palavra_secreta = "banana".upper()
    letras_corretas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0

    # len() retorna a quantidade de elementos em uma lista ou a quantidade de caracteres em uma frase
    print(f"\nA palavra secreta tem {len(letras_corretas)} letras!")
    print(letras_corretas)

    while (not enforcou and not acertou):

        # strip() -> Remove os espaços da string
        chute = input("\nEscolha uma letra: ").strip().upper()
        
        if (chute in palavra_secreta):
            posicao = 0

            # Esse FOR percorre toda a string e separa as posições de cada letra da palavra secreta
            for letra in palavra_secreta:

                # lower() -> Converte toda a string para o formato minúsculo
                # upper() -> Converte toda a string para o formato maiusculo
                if (chute == letra):
                    letras_corretas[posicao] = letra
                posicao += 1

            if (chute in letras_corretas):
                print(f"\nNice! Você acertou {letras_corretas.count(chute)} letra(s).")
                print("Veja como ficou a palavra secreta:")
        else:
            erros += 1
            print(f"Ops, você errou! Faltam {6-erros} tentativas.")

        enforcou = erros == 6
        acertou = "_" not in letras_corretas
        print(letras_corretas)
        print(f"Quantidade de letras ocultas: {letras_corretas.count("_")}")

if (__name__ == "__main__"):
    jogar()