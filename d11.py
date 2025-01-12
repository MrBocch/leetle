def solve(s):
  t = s.replace(" ", '')
  t = t.replace(",", '')
  t = t.replace(":", '')
  t = t.replace("?", '')
  t = t.lower()

  return list(t) == list(t)[::-1]

# python strings has this method, isalnum()
# it seems like pythonic code is not using maps and filters but
# this: [<value> <for thing in things> <if filter>]
