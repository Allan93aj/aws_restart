import random

print("Bem-vindo ao adivinhar o número!")
print("As regras são simples. Vou pensar em um número e você tentará adivinhá-lo.")

number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = input("Adivinhe um número entre 1 e 10: ")
    if int(guess) == number:
        print("Você adivinhou {}. Está correto! Você ganha!".format(guess))
        isGuessRight = True
    else:
        print("Você adivinhou {}. Desculpe, não é isso. Tente novamente.".format(guess))