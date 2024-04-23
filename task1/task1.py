import argparse
import sys


n = int(sys.argv[1])
m = int(sys.argv[2])
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
