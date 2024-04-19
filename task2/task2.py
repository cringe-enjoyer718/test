import math
circle_file = 'circle.txt'
points_file = 'points.txt'

# Функция для определения положения точки относительно окружности
def check_point(px, py, cx, cy, r):
    distance = math.sqrt((px - cx) ** 2 + (py - cy) ** 2)

    if distance < r:
        return 1  # Точка внутри окружности
    elif distance == r:
        return 0  # Точка на окружности
    else:
        return 2  # Точка вне окружности


# Считываем данные из файла (координаты центра и радиуса окружности)
with open(circle_file, 'r') as file:
    cx, cy = map(float, file.readline().split())
    r = float(file.readline())

# Считываем координаты точек из файла
with open(points_file, 'r') as file:
    points = [list(map(float, line.split())) for line in file]

# Проверяем положение каждой точки и выводим результат
for px, py in points:
    result = check_point(px, py, cx, cy, r)
    print(result)
