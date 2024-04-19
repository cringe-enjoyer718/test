import argparse

parser = argparse.ArgumentParser(description="ввод интервала и числа кругового массива")
parser.add_argument("n", help="1 parametr - число массива n")
parser.add_argument("m", help="2 parametr - интервал")
args = parser.parse_args()
n = int(args.n)
m = int(args.m)
array = m * [int(i) for i in range(1, n + 1)]
array.append(1)
print(array)
array2 = [' ']
array3 = []
count = 0
while array2[-1] != 1:
    array2.clear()
    for j in range(count, m + count):
        array2.append(array[j])
        count += 1
    array2_copy = array2.copy()
    array3.append(array2_copy)
    count -= 1
for q in range(len(array3)):
    print(array3[q][0], end='')