# 6: Faca um programa que receba do usuario um vetor com 10 posicoes. Em seguida devera
# ser impresso o maior e o menor elemento do vetor

numeros = [0,1,2,3,4,5,6,7,8,9]
maior = -9999999999
menor = 9999999999
indice = 0

while indice <= 9:
    numeros[indice] = float(input("Digite o número: "))

    if maior < numeros[indice]:
        maior = numeros[indice]
    
    if menor > numeros[indice]:
        menor = numeros[indice]

    indice +=1

print(f"maior: {maior}")
print(f"menor: {menor}")