def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def encontrar_primos_em_torno(n):
    menor_primo = n
    while True:
        if eh_primo(menor_primo):
            break
        menor_primo += 1

    maior_primo = n
    while True:
        if eh_primo(maior_primo):
            break
        maior_primo -= 1

    return menor_primo, maior_primo

n = int(input("Digite um número inteiro: "))

menor, maior = encontrar_primos_em_torno(n)
print(f"O menor número primo maior ou igual a {n} é: {menor}")
print(f"O maior número primo menor ou igual a {n} é: {maior}")
