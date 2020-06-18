'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n):
#   if n < 0:
#     return 0
#   elif n == 0:
#     return 1
#   else:
#     return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)

'''
cache is set up as a list comprehension for n 'cookies':
[0 for i in range(n+1)]
'''

def eating_cookies(n, cache=None):
  if not cache:
    cache = [0 for i in range(n+1)]
  if n < 0:
    return 0
  elif n == 0:
    return 1
  elif cache[n] > 0:
    return cache[n]
  else:
    cache[n] = eating_cookies(n-3, cache) + eating_cookies(n-2, cache) + eating_cookies(n-1, cache)
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 500

    print('Should be 1306186569702186634983475450062372018715120191391192207156664343051610913971927959744519676992404852130396504615663042713312314219527')
    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
