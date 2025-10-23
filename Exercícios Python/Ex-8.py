n = int(input("Valor de n: "))

fibonacci = [0, 1]

while len(fibonacci) < n:
    proximo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo)

print("Resultado:", " ".join(str(num) for num in fibonacci[:n]))
