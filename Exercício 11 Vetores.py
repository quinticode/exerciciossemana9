# 11. Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encon-
# tram o maior e o menor valor.

numeros = [0,1,2,3,4]
indice = 0 
maior = float('-inf') # infinito negativo
menor = float('inf') # infinito positivo
posMaior = 0
posMenor = 0

while indice <= 4:
    numeros[indice] = float(input("Por favor, digite um número: "))
        
    if maior < numeros[indice]:
        maior = numeros[indice]
        posMaior = indice
    
    if menor > numeros[indice]:
        menor = numeros[indice]
        posMenor = indice

    indice += 1

print(numeros)

print(f"A posição do menor é: {posMenor}, de 0 a 4")
print(f"A posição do maior é: {posMaior}, de 0 a 4")

    
