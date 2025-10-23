print("-- Verificador de sequências -- ")

a = [int(x) for x in input("Digite a primeira sequência: ")]
b = [int(x) for x in input("Digite a segunda sequência: ")]

contador = 0

for i in range(len(b) - len(a) + 1):
    if b[i : i + len(a)] == a:
        contador += 1

print("A primeira sequência aparece", contador, "vez(es) na segunda.")
