# not very pythonic in my opinion

def solve(s):
  rs = s.split(" ")[::-1]
  return [' '.join(rs)][0]
