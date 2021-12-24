def sort(n):
  n = str(n).ljust(4, "0")
  num = "".join(sorted([i for i in n]))
  return [int(num), int(num[::-1])]

def karp(n):
  count = -1

  last = n

  while True:

    smaller,bigger = sort(last)

    answer = bigger-smaller
    count += 1

    if answer==last:
      return count
    else:
      last = answer

  return count


print(karp(5200))