## it's a hash map
def minimumDistance(a):
 
    hmap = dict()
    minDistance = 10**9
    previousIndex = 0
    currentIndex = 0
 
    for i in range(len(a)):
 
        if a[i] in hmap:
            currentIndex = i
 
            previousIndex = hmap[a[i]]
 
            minDistance = min((currentIndex -
                        previousIndex), minDistance)
 
        hmap[a[i]] = i
 
    if minDistance == 10**9:
        return -1
    return minDistance


print(minimumDistance([2, 5, 3, 4, 5, 2]))