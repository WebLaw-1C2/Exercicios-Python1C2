vetor = []

for i in range (8):
    try:
        num = int(input(f"Escreva o {i + 1} ° número: " ))
        vetor.append(num)
    except ValueError:
        print("Digite apenas números inteiros!")
        exit()


print("A lista de números é: ", vetor)

vetorP = []
vetorN = []

for num in vetor:
    if num < 0:
        vetorN.append(num)
    else:
        vetorP.append(num)

print("A lista de números positivos é: ", vetorP)
print("A lista de números negativos é: ", vetorN)
