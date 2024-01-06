import adivinhacao
import forca

print("-=-=-=-=-=-=-=-")
print("ESCOLHA O JOGO")
print("-=-=-=-=-=-=-=-")

print("\n(1) JOGO DA ADIVINHAÇÃO")
print("(2) JOGO DA FORCA\n")

jogo = int(input("Selecione o jogo: "))

if (jogo == 1):
    adivinhacao.jogar()
elif (jogo == 2):
    forca.jogar()
else:
    print("Opção selecionada inválida, por favor, reinicie o launcher.")
    exit()