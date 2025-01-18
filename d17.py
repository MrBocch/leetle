# silly sintax that pass you when typing  
from collections import Counter
def solve(text):
  tally = Counter(text.lower())
  return sum([tally['a'], tally['e'],
              tally['i'], tally['o'],
              tally['u']])
