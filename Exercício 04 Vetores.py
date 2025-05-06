# 4: Faca um programa que leia um vetor de 8 posicoes e, em seguida, leia tambem dois va-
# lores X e Y quaisquer correspondentes a duas posicoes no vetor. Ao final seu programa
# devera ́ escrever a soma dos valores encontrados nas respectivas posicoes X e Y .

numeros = [0,1,2,3,4,5,6,7]
indice = 0

while indice <= 7:
    numeros[indice] = float(input("Digite o número: "))

    indice += 1


x = int(input("Digite a posição x: "))
y = int(input("Digite a posição y: "))

print(f"a soma é dos valores das posições é: {x + y}")