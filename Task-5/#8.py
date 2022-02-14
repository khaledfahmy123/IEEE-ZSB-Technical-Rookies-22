
def lol(n, s, t):
  for _ in rnage(n):
    counter = 0

    s_d = dict(zip(s, [0 for i in s]))
    t_d = dict(zip(t, [0 for i in t]))
    for i in s:
      s_d[i] = s_d[i] + 1
    for i in t:
      t_d[i] = t_d[i] + 1

    for i in s_d:
      if i not in t_d:
        counter += s_d[i]
      else:
        counter += abs(t_d[i]-s_d[i])
    for i in t_d:
      if i not in s_d:
        counter += t_d[i]
    print(c)




