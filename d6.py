def solve(nums):
  i = 0
  max_sum = 0
  while i < len(nums)-2:
    cur_sum = nums[i]
    j = i + 1
    while j < len(nums):
      cur_sum += nums[j]
      j += 1
      max_sum = max(max_sum, cur_sum)

    i += 1

  return max_sum

# ughh, im just tired from work okay
# first 3 attempts i was trying
# to solve it thinking, ohh, just return the max of all the list permutations sums
# not realising permutations does not mean, [1,2,3] -> [1,2] and [2,3] and [1,2,3]
# last chance i look at line 4, 'should it be -2 or -1?' i guessed wrong
# should have not left if for chance

# i did not guess wrong, did not think of
# case [1] and [1, 1]
def solve(nums):
  i = 0
  max_sum = nums[i]
  while i < len(nums):
    cur_sum = nums[i]
    j = i + 1
    while j < len(nums):
      cur_sum += nums[j]
      j += 1
      max_sum = max(max_sum, cur_sum)
    max_sum = max(max_sum, cur_sum)
    i += 1

  return max_sum

# did really bad today
# how would this functionally?
# take array, find every sub array, map sum function
# to each list, and return the max
