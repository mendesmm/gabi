import os


os.system("cls")


# pedindo para digitar o nome
nome = input("Digite seu nome: ")
# pedindo para digitar a idade
idade = int(input("Digite sua idade: "))

if idade >= 16 and idade < 18:
    print(f"{nome}, você pode votar, mas não pode dirigir")
elif idade >= 18:
    print(f"{nome}, você pode votar e dirigir")
else:
    print(f"{nome}, você não pode votar e nem pode dirigir")
