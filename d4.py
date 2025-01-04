def solve(nums):
  i = 0
  for n in sorted(nums):
    if i != n:
      return i 
    i += 1
  
  return i 
