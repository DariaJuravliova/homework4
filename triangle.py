def triangle_type(a, b, c):
    # Проверка существования треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник с такими сторонами не существует"

    # Определение типа треугольника
    if a != b and b != c and a != c:
        return "Треугольник разносторонний"
    elif a == b and b == c:
        return "Треугольник равносторонний"
    else:
        return "Треугольник равнобедренный"
print(triangle_type(a, b, c))
