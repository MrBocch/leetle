def solve(s1, s2):
  s1_tally = {}
  s2_tally = {}

  for c in s1:
    if c not in s1_tally:
      s1_tally[c] = 1
    else:
      s1_tally[c] += 1

  for c in s2:
    if c not in s2_tally:
      s2_tally[c] = 1
    else:
      s2_tally[c] += 1

  return s1_tally == s2_tally
# in ruby this is
# def s s1, s2
#   return s1.split("").tally == s2.split("").tally
# end
