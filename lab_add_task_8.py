a, b, c = [float(input()) for _ in range(3)]
triangle_type = "Треугольник не существует"

if a + b >= c and b + c >= a and a + c >= b:
    if a == b and b == c and c == a:
        triangle_type = "Треугольник существует, равностороний"
    elif a == b or b == c or c == a:
        triangle_type = "Треугольник существует, равнобедренный"
    else:
        triangle_type = "Треугольник существует, разносторонний"

print(triangle_type)