def solve(nums):
  tally = {}
  for n in nums:
    if n not in tally:
      tally[n] = 1
    else:
      tally[n] += 1

  max_num = nums[0]
  for n, times in tally.items():
    if tally[max_num] < times:
      max_num = n

  return max_num

# felt so fat after looking at the solutions lol, i prefer ruby or python

# look at the power of ruby
# def solve(nums)
#   return nums.tally.sort.last.first
