def solve(nums):
  poss = list(filter(g_zero, nums))

  i = 1
  for n in list(set(sorted(poss))):
    if i != n:
      return i
    else:
      i += 1

  return i

def g_zero(n):
  return n > 0
# next time for small functions like these
# i will use the lambda thing

# all the edge cases got me,
# like, what if zero in list
# and duplicate numbers
