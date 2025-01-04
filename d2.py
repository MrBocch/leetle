def solve(nums):
  tally = {}
  for n in nums:
    if n not in tally:
      tally[n] = 1
    else:
      tally[n] += 1

  for k, v in tally.items():
    if v == 1:
      return k
    

