sequencia1 = list(map(int, input("primeira sequencia: ").split()))
sequencia2 = list(map(int, input("segunda sequencia: ").split()))

i = j = 0
resultado = []

for _ in range(len(sequencia1) + len(sequencia2)):
    if j == len(sequencia2) or (i < len(sequencia1) and sequencia1[i] <= sequencia2[j]):
        resultado.append(sequencia1[i])
        i += 1
    else:
        resultado.append(sequencia2[j])
        j += 1

print("resultado:", *resultado)
