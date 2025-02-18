crt = tuple(map(int, input("Введите целые числа, разделенные пробелом: ").split()))

index = -1

for i in range(len(crt) - 1):
    if crt[i] % 2 == 0 and crt[i + 1] % 2 == 0:
        index = i + 1

if index != -1:
    print("Элементы, предшествующие последней паре соседних четных чисел:")
    print(crt[:index])
else:
    print("Пара соседних четных чисел не найдена.")

