# 7. Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima
# o vetor, o maior elemento e a posição que ele se encontra.

numeros = [0,1,2,3,4,5,6,7,8,9]
indice = 0 
posicao = 0
maior = -9999999999

while indice <= 9:
    numeros[indice] = int(input("Digite o número: "))

    if maior < numeros[indice]:
        posicao = indice
        maior = numeros[indice]
    
    indice += 1

print(f"numeros: {numeros}")
print(f"maior elemento: {numeros[posicao]}")
print(f"se encontra na posicao: {posicao}, de 0 a 9")