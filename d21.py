def solve(n):
  if n == 0:
    return 1 

  elif n == 1:
    return 1
  else:
    return n * solve(n-1)

# simple question today
