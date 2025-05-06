# 5: Leia um vetor de 10 posicoes. Contar e escrever quantos valores pares ele possui.

numeros = [0,1,2,3,4,5,6,7,8,9]
pares = 0
indice = 0

while indice <= 9:
    numeros[indice] = int(input("Digite o número: "))

    if numeros[indice] % 2 == 0:
        pares += 1

    indice += 1

print(f"voce deu {pares} numeros pares")