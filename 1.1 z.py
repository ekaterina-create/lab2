side1 = float(input('Введите длину первой стороны: '))
side2 = float(input('Введите длину второй стороны: '))
side3 = float(input('Введите длину третьей стороны: '))

half_perimeter = (side1 + side2 + side3) / 2

area = (
    half_perimeter
    * (half_perimeter - side1)
    * (half_perimeter - side2)
    * (half_perimeter - side3)
) ** 0.5

print(f'Площадь треугольника равна: {area:.2f}')