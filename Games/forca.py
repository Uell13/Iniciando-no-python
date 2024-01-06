def jogar():

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input("Escolha uma letra: ")
        
        posicao = 0
        for letra in palavra_secreta:       
            if (chute == letra):
                print(f"Encontrei a letra ({letra}) na posição {posicao}.")
            
            posicao = posicao + 1

if (__name__ == "__main__"):
    jogar()