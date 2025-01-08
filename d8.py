def solve(nums, target):

  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]

  return []
# i solved the leetcode version, O(n) wiht a hashmap
# but i did not fully remember how it went so decided
# to take easy route
