
nums = list(map(int, input("Digite os números separados por espaço: ").split()))

c = int(input("Digite o valor de C: "))

encontrou = False
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] * nums[j] == c:
            print(f"Resultado: {nums[i]} e {nums[j]}")
            encontrou = True
            break
    if encontrou:
        break

if not encontrou:
    print("Resultado: não existem tais números")
