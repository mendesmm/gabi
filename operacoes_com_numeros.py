import os

os.system("cls")

def calcular(numero1: float, numero2: float, operacao: str) -> float:
    if operacao == "/":
        return numero1 / numero2
    elif operacao == "*":
        return numero1 * numero2
    elif operacao == "-":
        return numero1 - numero2
    else:
        return numero1 + numero2


# lendo o numero1
numero1 = float(input("Digite o numero 1: "))
# lendo o numero2
numero2 = float(input("Digite o numero 2: "))
# lendo a operacao
operacao = input("Digite a operacao: ")

print(f"O resultado de {numero1} {operacao} {numero2} é: {calcular(numero1=numero1, numero2=numero2, operacao=operacao)}")