# sundays problem was hard
# 200. Number of Islands, dont even know where to start
def solve(nums):
  sum = 0
  running = []
  for n in nums:
    running.append(n + sum)
    sum += n

  return running

# i think i know how to solve this with 
# list comprehensions but it would be n^2
