# Функция находит длину отрезка достраивая до треугольника и вычисляя длину по теореме Пифагора
def long(x1, y1, x2, y2):
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    c = (a ** 2 + b ** 2) ** (1/2)
    return c
x1, y1 = map(int, input("Введите координаты первой точки: ").split())
x2, y2 = map(int, input("Введите координаты второй точки: ").split())
x3, y3 = map(int, input("Введите координаты третьей точки: ").split())
a = long(x1, y1, x2, y2)
b = long(x1, y1, x2, y2)
c = long(x2, y2, x3, y3)
print(a + b + c)
