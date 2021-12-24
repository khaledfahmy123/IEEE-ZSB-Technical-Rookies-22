def record(arr, n):
    minVal = arr[0]
    maxVal = arr[0]
    maxCount = 0
    minCount = 0

    for i in range(len(arr)):
        if arr[i] > maxVal:
            maxVal = arr[i]
            maxCount += 1
        elif arr[i] < minVal:
            minVal = arr[i]
            minCount += 1

    print([maxCount, minCount])

arr = [10, 5, 20, 20, 4, 5, 2, 25, 1]
n = 9
record(arr, n)