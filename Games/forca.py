# Text Sequence Type — str
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

def jogar():

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):

        # strip() -> Remove os espaços da string
        chute = input("Escolha uma letra: ").strip()
        
        posicao = 0

        # Esse FOR percorre toda a string e separa as posições de cada letra da palavra secreta
        for letra in palavra_secreta:

            # lower() -> Converte toda a string para o formato minúsculo
            # upper() -> Converte toda a string para o formato maiusculo
            if (chute.lower() == letra.lower()):

                # Formatando a string para receber os dados das variaveis
                print(f"Encontrei a letra ({chute}) na posição {posicao}.")
            
            posicao += 1

if (__name__ == "__main__"):
    jogar()