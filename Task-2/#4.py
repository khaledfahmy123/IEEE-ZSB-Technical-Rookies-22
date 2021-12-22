def minDist(arr, n):
    mp = {}
 
    minDict = 0
    
    for i in range(n):
 
        if arr[i] not in mp.keys():
            mp[arr[i]] = i
        else:
            if minDict == 0 :
                minDict = i-mp[arr[i]]
            else:
                minDict = min(minDict, i-mp[arr[i]])
 
    return minDict


arr = [int(a) for a in input("enter the list: \n").split(" ")]
print(minDist(ar, len(ar)))