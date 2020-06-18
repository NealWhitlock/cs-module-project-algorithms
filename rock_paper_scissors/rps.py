#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Create list for outcomes
  outcomes = []
  # Loop n times
  for i in range(n+1):
    if i == 0:
      outcomes.append([])
  # In each iteration of the loop, take anything in the list and append
    else:
      for j in range(len(outcomes)):
        new = outcomes.pop(0)
        # rock
        outcomes.append(new + ['rock'])
        # paper
        outcomes.append(new + ['paper'])
        # and scissors to what is already in there
        outcomes.append(new + ['scissors'])
  # Return list
  return outcomes


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')