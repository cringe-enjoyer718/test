import argparse
import sys
#parser = argparse.ArgumentParser(description="ввод чисел массива")
#parser.add_argument("file", help="1 parametr - путь к файлу с числами массива")
# Считываем числа из файла и записываем их в массив
#args = parser.parse_args()
file = sys.argv[1]
with open(file, 'r') as file:
    nums = [int(line) for line in file]


# Функция для определения минимального количества ходов
def min_moves(nums):
    sum = 0
    ct=0
    moves = 0
    for a in nums:
        sum += a
        ct +=1
    sred_arif = round(sum/ct)
    for a in nums:
        if a > sred_arif:
            moves += (a - sred_arif)
        elif a < sred_arif:
            moves += (sred_arif - a)
        else:
            moves += 0
    return moves


# Вызываем функцию и выводим результат
moves = min_moves(nums)
print("Минимальное количество ходов для приведения всех элементов к одному числу:", moves)
