def soma(n):
    return n * (n + 1) // 2 

n = int(input("Digite um número inteiro: "))
resultado = soma(n)
print(f"A soma de 0 até {n} é {resultado}")
