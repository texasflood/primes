import math
def eratosthenes2(n):
  multiples = set()
  for i in range(2, n+1):
    if i not in multiples:
      yield i
      multiples.update(range(i*i, n+1, i))

my_list = list(eratosthenes2(250000000))
print(len(my_list))
