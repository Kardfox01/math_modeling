a, b = int(input("Первое число: ")), int(input("Второе число: "))
if b != 0:
    remainder = a % b
    answer = a / b
    print(
        f"Остаток: {remainder}" if remainder else f"Первое число делится на второе"
    )
    print("Частное:", answer)
else:
    print("Второе число равно нулю")