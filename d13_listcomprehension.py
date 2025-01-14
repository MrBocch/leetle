def solve(nums):
  return [n+sum(nums[0:i]) for i, n in enumerate(nums)]

# the time complexity is bad compared to the imperative solution
# because the sum of nums[0:i-1] 
# would be recalculated over and over instead of 
# incrementing a sum variable
# but looks preetier so its better
