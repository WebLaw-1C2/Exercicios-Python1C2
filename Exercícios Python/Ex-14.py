def p(n):
    if n < 1:
        return None
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

n = int(input("Digite um número inteiro: "))

resultado = p(n)

if resultado is None:
    print("O número deve ser maior ou igual a 1.")
elif resultado:
    print(f"{n} é primo.")
else:
    print(f"{n} não é primo.")
