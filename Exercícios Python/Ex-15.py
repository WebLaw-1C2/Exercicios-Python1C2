print("Veificador de anos bissextos")

while True:
    try:
        ano = int(input("Digite um ano: "))
        break

    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números inteiros.")

if ano % 400 == 0:
    print(f"{ano} é um ano bissexto")
elif ano % 4 == 0 and ano % 100 != 0:
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")
