import random as r
import time as t

mylist = ["pedra", "papel", "tesoura"]

print("Escreva pedra, papel, tesoura!")

Escolha = input("Sua Escolha: ")

pergunta = print("Está foi sua escolha correto?: " + Escolha)
resposta = input("Sim ou Não?: ")
if resposta == "Sim":
    print("")
    print("Carregando")
    print("")
    t.sleep(2)

    adv = r.choice(mylist)


    if adv == "pedra":
        if Escolha == "papel":
            print("Você venceu!")
        if Escolha == "pedra":
            print("Empate")
        if Escolha == "tesoura":
            print("Você perdeu")

    if adv == "papel":
        if Escolha == "papel":
            print("Empate")
        if Escolha == "pedra":
            print("Você perdeu")
        if Escolha == "tesoura":
            print("Você venceu!")

    if adv == "tesoura":
        if Escolha == "papel":
            print("Você perdeu")
        if Escolha == "pedra":
            print("Você venceu!")
        if Escolha == "tesoura":
            print("Empate")

t.sleep(5)
