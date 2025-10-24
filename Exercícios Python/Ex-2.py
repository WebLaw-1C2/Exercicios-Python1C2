medida = str(input("deseja realizar a metragem em celcius (c) ou em fairenheit (f)?"))

if medida == "c":
    temperatura = float(input ("insira a temperatura em fairenheits:  "))
    celcius = 5/9 * (temperatura - 32)
    print("a temperatura ", temperatura, "em celcius é: ", celcius)

elif medida == "f":
    temperatura = float(input ("insira a temperatura em celcius:  "))
    feirenheits = (temperatura * 9 + 160)/5
    print("a temperatura ", temperatura, "em fairenheits é:", feirenheits)
    
else:
    print("insira c ou f")
