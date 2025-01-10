def solve(nums, k):
  return list(map(max, sub_arrays(nums, k)))

def sub_arrays(lst, k):
  return [lst[i:i+k] for i in range(len(lst) - k + 1)]

# considering the disaster i had with subarrays last
# time, i thought to ask chatgpt for a function that takes a list and K
# and returns the subarrays of size, k
# from there its just maping (max) over it.
# using chatgpt is cheating so i wont do it again.
