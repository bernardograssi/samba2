def fun(lis):
  even = []
  odd = []
  for i in lis:
    if i % 2 == 0:
      even += [i]
    else:
      odd += [i]
  lis = even + odd

  even_idx = len(even) - 1
  odd_idx = len(lis) - 1
  for i in range(even_idx + 1, odd_idx, 1):
    pos = i
    for j in range(i + 1, odd_idx):
      if lis[j] < lis[pos]:
        pos = j
    lis[i], lis[pos] = lis[pos], lis[i]
  
  for i in range(0, even_idx, 1):
    pos = i
    for j in range(i + 1, even_idx + 1):
      if lis[j] > lis[pos]:
        pos = j
    lis[i], lis[pos] = lis[pos], lis[i]
  
  return lis
