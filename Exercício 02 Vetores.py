# 2. Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos.
numeros = [0,0,0,0,0,0]
indice = 0

while indice <= 5:

    numeros[indice] = int(input("Digite os valores: "))
    indice += 1

print(numeros)