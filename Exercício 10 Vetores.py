# 10. Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
# juntamente com o maior, o menor e a média dos valores.

numeros = [0,1,2,3,4]
indice = 0
maior = float('-inf') # infinito negativo
menor = float('inf') # infinito positivo
somaNumeros = 0

while indice <= 4:
    numeros[indice] = float(input("Diga-me o número: "))

    if maior < numeros[indice]:
        maior = numeros[indice]

    if menor > numeros[indice]:
        menor = numeros[indice]

    somaNumeros += numeros[indice]

    indice += 1

print(numeros)
print(f"Maior: {maior} \nMenor: {menor} \nMédia: {somaNumeros / (indice)}")

