# 3. Ler um conjunto de numeros reais, armazenando-o em vetor e calcular o quadrado das
# componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm 10
# elementos cada. Imprimir os conjuntos.

numeros = [0,0,0,0,0,0,0,0,0,0]
quadrados = [0,0,0,0,0,0,0,0,0,0]
indice = 0

while indice <= 9:

    numeros[indice] = int(input("Digite o número: "))
    quadrados[indice] = numeros[indice] ** 2
    indice += 1

print(f"Números: {numeros}")
print(f"Quadrados: {quadrados}")
