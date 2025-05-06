# 1: Faça um programa que possua um vetor denominado A que armazene 6 numeros inteiros. O programa deve executar os seguintes passos:

# (a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.

# (b) Armazene em uma variavel inteira (simples) a soma entre os valores das posicoes
#  A[0], A[1] e A[5] do vetor e mostre na tela esta soma.

# (c) Modifique o vetor na posicao 4, atribuindo a esta posicao o valor 100.

# (d) Mostre na tela cada valor do vetor A, um em cada linha.

A = [1,0,5,-2,-5,7]
soma = A[0] + A[1] + A[5]
print(f"soma a0 a1 a5: {soma}")
A[4] = 100

print(f"todo o vetor:\n{A[0]},\n{A[1]},\n{A[2]},\n{A[3]},\n{A[4]},\n{A[5]}")