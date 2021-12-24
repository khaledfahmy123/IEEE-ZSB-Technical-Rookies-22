def freq(arr, n):
    Hash = dict()
    count = 0
    for i in range(n):
        if arr[i] in Hash.keys():
            Hash.pop(arr[i]) 
            count += 1
        else:
            Hash[arr[i]] = 1

    return count

arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = len(arr)

print(freq(arr, n))