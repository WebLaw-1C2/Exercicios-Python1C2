while True:
    try:
        n1 = int(input("Digite um número inteiro: "))
        n2 = int(input("Digite outro número inteiro: "))
        operador = str(input("Digite o operador (+, -, , /): "))
        break

    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números inteiros.")

if operador == "+":
    print(f"{n1} + {n2} = {n1 + n2}")

elif operador == "-":
    print(f"{n1} - {n2} = {n1 + n2}")

elif operador == "/":
    print(f"{n1} / {n2} = {n1 + n2}")

else:
    print(f"{n1} {n2} = {n1 + n2}")
