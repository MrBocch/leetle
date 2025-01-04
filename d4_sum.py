# when you dont solve it first try, you recieve a hint
# this solution is much prettier

def solve(nums):
  return sum(range(len(nums)+1)) - sum(nums)
