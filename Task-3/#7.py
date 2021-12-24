def freq(arr, n):
    Hash = dict()
    for i in range(n):
        if arr[i] in Hash.keys():
            Hash[arr[i]] += 1
        else:
            Hash[arr[i]] = 1
 
    max_count = 0
    res = -1
    for i in Hash:
        if (max_count < Hash[i]):
            res = i
            max_count = Hash[i]
        elif (max_count == Hash[i]) and res > i:
            res = i
    return res

arr = [ 1,2,3,4,5,4,3,2,1,3,4]
n = len(arr)
print(freq(arr, n))