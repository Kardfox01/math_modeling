a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b**2 - 4 * a * c
if D > 0:
    print("x₁ =", (-b + D**.5) / 2 * a)
    print("x₂ =", (-b - D**.5) / 2 * a)
elif D == 0:
    print("x = ", (-b) / (2 * a))
else:
    print("Корней нет")