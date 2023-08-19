import pyautogui
import random as r
import time as t

print("")
print("1 - Spammer")
print("2 - Calculadora")
print("3 - Pedra papel tesoura")
print("")

opcoes = input("Escolha uma das opções: ")

# opcao 1 de escolha
if opcoes == '1':
    i = 0
    msg = input("Coloque sua mensagem: ")
    nmr = input("Coloque a quantidade de vez a ser repetida: ")

    while i <= int(nmr):

        pyautogui.typewrite(msg)
        pyautogui.press("Enter")
        i+=1
# opcao 2 de escolha
if opcoes == '2':
    print("")
    print("1 - Adicionar")
    print("2 - Subtrair")
    print("3 - Dividir")
    print("4 - Multiplicar")
    print("")

    pergunta = input("Escolha um dos itens acima: ")

    valor1 = input("Digite o primeiro valor: ")
    valor2 = input("Digite o segundo valor: ")

    Valorfim1 = int(valor1)
    Valorfim2 = int(valor2)

    if pergunta == "1":
        print(Valorfim1 + Valorfim2)
    elif pergunta == "2":
        print(Valorfim1 - Valorfim2)
    elif pergunta == "3":
        print(Valorfim1 / Valorfim2)
    elif pergunta == "4":
        print(Valorfim1 * Valorfim2)

# opcao 3 de escolha
if opcoes == '3':

    mylist = ["pedra", "papel", "tesoura"]

    escolha = input("Escolha pedra, papel ou tesoura: ")

if ("pedra", "papel", "tesoura"):
    print("")
    print("Carregando")
    print("")
    t.sleep(2)

adv = r.choice(mylist)

if adv == "pedra":
    if escolha == "pedra":
        print(adv + " Empate!")
    if escolha == "papel":
        print(adv + " Você ganhou!")
    if escolha == "tesoura":
        print(adv + " Você perdeu!")


if adv == "papel":
    if escolha == "papel":
        print(adv + " Empate!")
    if escolha == "tesoura":
        print(adv + " Você ganhou!")
    if escolha == "pedra":
        print(adv + " Você perdeu!")

if adv == "tesoura":
    if escolha == "tesoura":
        print(adv + " Empate!")
    if escolha == "pedra":
        print(adv + " Você ganhou!")
    if escolha == "papel":
        print(adv + " Você perdeu!")

