# 8. Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule
# e imprima a média geral.

notas = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
indice = 0
somaNotas = 0

while indice <= 14:
    notas[indice] = float(input("Digite a nota " + str(indice + 1) + ": " ))
    somaNotas += notas[indice]
    indice += 1

print(f"Média geral: {somaNotas/15}")