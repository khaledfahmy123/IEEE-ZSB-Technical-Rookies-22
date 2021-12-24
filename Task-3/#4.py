def kangaroo(x1, v1, x2, v2):
    if v1 == v2 and x1==x2:
        return("YES")
    elif v1 == v2 or x1 == x2:
        return("NO")
    elif (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) > 0:
        return("YES")
    else:
        return("NO")

kang(43, 2, 70, 2)