def diff():
	n = int(input("enter one dimension of the matrix: "))
	arr = []
	
	for i in range(n):
		arr.append([int(a) for a in input(f"enter row {i+1} numbers: ").split(" ")])

	sum1 = sum(arr[i][i] for i in range(n))
	sum2 = sum(arr[i][n-i-1] for i in range(n))
	print(abs(sum1-sum2))

diff()


## Hacker Rank Version

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sum1 = sum(arr[i][i] for i in range(n))
    sum2 = sum(arr[i][n-i-1] for i in range(n))
    return abs(sum1-sum2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()