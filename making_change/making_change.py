#!/usr/bin/python

import sys

def making_change(amount, denominations):
  if amount < 0:
    return 0
  elif amount == 0:
    return 1
  else:
    total = 0
    for i in range(len(denominations)):
      change = denominations[i]
      if change > amount:
        continue
      else:
        result = making_change(amount - change, denominations[i:])
        if result > 0:
          total += result
    return total


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")