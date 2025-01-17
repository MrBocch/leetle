# should have solved it, its not even hard
def solve(nums):
  sn = sorted(nums)
  seq = [0]
  idx = 0
  for i in range(len(sn)-2):
    if sn[i]+1 == sn[i+1]:
      seq[idx] += 1
    else:
      seq.append(0)
      idx += 1

  return max(seq)

