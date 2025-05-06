import random

numerosHumano = [0,0,0,0,0,0]
numerosAposta = [0,0,0,0,0,0]
indiceHumano = 0
indiceAposta = 0
indiceComparador = 0

acertos = 0

while indiceHumano <= 5:
    numerosHumano[indiceHumano] = int(input(f"Digite o numero {indiceHumano + 1} da sua aposta: "))
    indiceHumano += 1

while indiceAposta <= 5:
    numerosAposta[indiceAposta] = random.randint(1,60)
    indiceAposta += 1

indiceAposta = 0

while indiceComparador <= 5:
    
    while indiceAposta <= 5:

        if numerosHumano[indiceComparador] == numerosAposta[indiceAposta]:

            acertos += 1

        indiceAposta += 1

    indiceComparador += 1
    indiceAposta = 0

print(f"Numeros Jogados:  {numerosHumano}")
print(f"Numeros Da MEGA SENA: {numerosAposta}")
print(f"Acertos: {acertos}")