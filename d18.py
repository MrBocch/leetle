# only solved this because i went to
# a repl, and manually changed it into it worked
# wich feels against the rules because you are only supposed
# to get 5 tries. Stop cheating
def solve(n):
  pascal = []
  while len(pascal) != n:
    if len(pascal) == 0:
      pascal.append([1])
      continue
    if len(pascal) == 1:
      pascal.append([1,1])
      continue
    if len(pascal) == 2:
      pascal.append([1,2,1])
      continue

    prev = pascal[-1]
    curr = []
    for i in range(len(prev)+1):
        if i == 0:
            curr.append(1)
            continue
        if i+1 == len(prev)+1:
            curr.append(1)
            continue
        curr.append(prev[i]+prev[i-1])
    pascal.append(curr)

  return pascal
