# 9. Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a
# quantidade de números negativos e a soma dos números positivos desse vetor.

numeros = [0,1,2,3,4,5,6,7,8,9]
indice = 0
negativos = 0
somaPositivos = 0

while indice <= 9:
    
    numeros[indice] = float(input("Digite um número real: "))
    
    if numeros[indice] < 0:
        negativos += 1
    else:
        somaPositivos += numeros[indice]
    
    indice += 1
    
print(numeros)
print(f"\nVocê digitou {negativos} números negativos. \nA soma dos números positivos é: {somaPositivos}")