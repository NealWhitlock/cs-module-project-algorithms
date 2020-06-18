#!/usr/bin/python

import sys

def making_change(amount, denominations):
  coins = [0, 0, 0, 0, 0]
  count_list = set()

  def helper_function(amount, coins, count_list, denom):

    if amount - (coins[0]*denom[0] + coins[1]*denom[1] + coins[2]*denom[2] + 
                 coins[3]*denom[3] + coins[4]*denom[4]) >= denom[4]:
      coins_50 = coins.copy()
      coins_50[4] += 1
      helper_function(amount, coins_50, count_list, denom)

    if amount - (coins[0]*denom[0] + coins[1]*denom[1] + coins[2]*denom[2] + 
                 coins[3]*denom[3] + coins[4]*denom[4]) >= denom[3]:
      coins_25 = coins.copy()
      coins_25[3] += 1
      helper_function(amount, coins_25, count_list, denom)

    if amount - (coins[0]*denom[0] + coins[1]*denom[1] + coins[2]*denom[2] + 
                 coins[3]*denom[3] + coins[4]*denom[4]) >= denom[2]:
      coins_10 = coins.copy()
      coins_10[2] += 1
      helper_function(amount, coins_10, count_list, denom)

    if amount - (coins[0]*denom[0] + coins[1]*denom[1] + coins[2]*denom[2] + 
                 coins[3]*denom[3] + coins[4]*denom[4]) >= denom[1]:
      coins_5 = coins.copy()
      coins_5[1] += 1
      helper_function(amount, coins_5, count_list, denom)

    if amount - (coins[0]*denom[0] + coins[1]*denom[1] + coins[2]*denom[2] + 
                 coins[3]*denom[3] + coins[4]*denom[4]) >= denom[0]:
      coins_1 = coins.copy()
      coins_1[0] += 1
      helper_function(amount, coins_1, count_list, denom)

    if amount - (coins[0]*denom[0] + coins[1]*denom[1] + coins[2]*denom[2] + 
                 coins[3]*denom[3] + coins[4]*denom[4]) == 0:
      count_list.add(tuple(coins))

    #print(count_list)

    return len(count_list)

  count = helper_function(amount, coins, count_list, denominations)

  return count


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")