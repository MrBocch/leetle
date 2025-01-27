# silly me did not think about 
# if i is power of 2, this condition
# while i < n:
# wont be true, then it will return false when it shouldn't
def solve(n):
  i = 1

  while i <= n:
    if i == n:
      return True
    i *= 2

  return False
